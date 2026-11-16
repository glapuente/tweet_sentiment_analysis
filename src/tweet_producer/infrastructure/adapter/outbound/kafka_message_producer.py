from confluent_kafka import Producer

from tweet_producer.application.port.outbound.outbound_message_repository import (
    OutboundMessageRepository,
)
from tweet_producer.domain.model.message import ProcessedMessage
from tweet_producer.infrastructure.config.kafka_configuration import KafkaConfiguration


class KafkaMessageProducer(OutboundMessageRepository):
    def __init__(
        self,
        kafka_topic: str,
        kafka_configuration: KafkaConfiguration,
    ):
        super().__init__()
        self._kafka_topic = kafka_topic
        self._kafka_configuration = kafka_configuration

    def append_message(self, processed_message: ProcessedMessage) -> None:
        producer = Producer(
            {
                "bootstrap.servers": self._kafka_configuration.kafka_connection_url,
            }
        )
        producer.produce(self._kafka_topic, processed_message.to_json())
        producer.flush()
