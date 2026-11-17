import pyspark.sql.functions as F
from pyspark.sql import SparkSession

from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.application.port.outbound.database_message_repository import (
    DatabaseMessageRepository,
)
from tweet_producer.application.use_cases.sentiment_analysis import SentimentAnalyzer
from tweet_producer.domain.model.common import dataclass_to_pyspark_schema
from tweet_producer.domain.model.message import (
    ProcessedMessage,
)
from tweet_producer.domain.model.sentiment_analysis import SentimentSchema
from tweet_producer.infrastructure.config.kafka_configuration import KafkaConfiguration


class SparkKafkaMessageConsumer(MessageRepository):
    def __init__(
        self,
        kafka_topic: str,
        kafka_configuration: KafkaConfiguration,
        spark_session: SparkSession,
        database_message_repository: DatabaseMessageRepository,
    ):
        super().__init__()
        self._kafka_topic = kafka_topic
        self._kafka_configuration = kafka_configuration
        self._spark_session = spark_session
        self._sentiment_analyzer = SentimentAnalyzer()
        self._database_message_repository = database_message_repository

    def fetch_messages(self, message_per_second: float):
        streaming_df = (
            self._spark_session.readStream.format("kafka")
            .option(
                "kafka.bootstrap.servers",
                self._kafka_configuration.kafka_connection_url,
            )
            .option("subscribe", self._kafka_topic)
            .option("startingOffsets", "earliest")
            .load()
        )

        query = (
            streaming_df.withColumn(
                "json_message",
                F.from_json(
                    F.col("value").cast("string"),
                    dataclass_to_pyspark_schema(ProcessedMessage),
                ),
            )
            .withColumn(
                "sentiment_analysis",
                F.udf(
                    self._sentiment_analyzer.analyze_sentiment,
                    dataclass_to_pyspark_schema(SentimentSchema),
                )(F.col("json_message.text")),
            )
            .select(
                *[
                    F.col(f"json_message.{col}")
                    for col in ProcessedMessage.message_fields()
                ],
                F.col("sentiment_analysis.*"),
                F.col("topic"),
                F.col("partition"),
                F.col("offset"),
                F.col("timestamp"),
            )
            .writeStream.foreachBatch(self._database_message_repository.save_message)
            .outputMode("append")
            .start()
        )
        query.awaitTermination()
