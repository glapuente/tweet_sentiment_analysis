from typing import Generator

from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.domain.model.message import ProcessedMessage
from tweet_producer.infrastructure.config.kafka_configuration import KafkaConfiguration


class KafkaMessageConsumer(MessageRepository):
    def __init__(
        self,
        kafka_topic: str,
        kafka_configuration: KafkaConfiguration,
    ):
        super().__init__()
        self._kafka_topic = kafka_topic
        self._kafka_configuration = kafka_configuration


    def fetch_messages(self, message_per_second: float) -> Generator[ProcessedMessage]:
        pass