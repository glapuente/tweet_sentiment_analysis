from abc import ABC, abstractmethod

from tweet_producer.domain.model.message import ProcessedMessage


class OutboundMessageRepository(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def append_message(self, processed_message: ProcessedMessage) -> None: ...
