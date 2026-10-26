from abc import ABC, abstractmethod

from tweet_producer.domain.model.message import ProcessedMessage


class MessageRepository(ABC):
    def __init__(
        self,
    ):
        self._class_name = "MessageRepository"


    @abstractmethod
    def fetch_messages(
        self,
        message_per_second: int | None = None,
    ) -> list[ProcessedMessage]:
        ...