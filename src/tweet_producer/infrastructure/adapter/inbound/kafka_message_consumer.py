import pyspark.sql.functions as F
from pyspark.sql import SparkSession

from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.domain.model.message import (
    ProcessedMessage,
    dataclass_to_pyspark_schema,
)
from tweet_producer.infrastructure.config.kafka_configuration import KafkaConfiguration


class SparkKafkaMessageConsumer(MessageRepository):
    def __init__(
        self,
        kafka_topic: str,
        kafka_configuration: KafkaConfiguration,
        spark_session: SparkSession,
    ):
        super().__init__()
        self._kafka_topic = kafka_topic
        self._kafka_configuration = kafka_configuration
        self._spark_session = spark_session

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
            .select(
                F.col("json_message.*"),
                F.col("topic"),
                F.col("partition"),
                F.col("offset"),
                F.col("timestamp"),
            )
            .writeStream.format("console")
            .outputMode("append")
            .option("truncate", False)
            .start()
        )
        query.awaitTermination()
