from typing import Generator

from pyspark.sql import SparkSession

from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.domain.model.message import ProcessedMessage
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
        print("LLEGA")

        df = self._spark_session.createDataFrame([
            (1, 2., 'string1', "2000, 1, 1", "2000, 1, 1, 12, 0"),
            (2, 3., 'string2', "date(2000, 2, 1", "2000, 1, 2, 12, 0"),
            (3, 4., 'string3', "date(2000, 3, 1", "2000, 1, 3, 12, 0")
        ], schema='a long, b double, c string, d string, e string')
        print(df.show())

        print(str(self._kafka_configuration))