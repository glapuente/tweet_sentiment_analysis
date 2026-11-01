from tweet_producer.application.port.outbound.outbound_message_repository import OutboundMessageRepository
from tweet_producer.domain.model.message import ProcessedMessage


class KafkaMessageRepository(OutboundMessageRepository):
    def __init__(
        self,
        kafka_topic: str,
    ):
        super().__init__()
        self._kafka_topic = kafka_topic


    def append_message(self, processed_message: ProcessedMessage) -> None:
        raise NotImplemented
