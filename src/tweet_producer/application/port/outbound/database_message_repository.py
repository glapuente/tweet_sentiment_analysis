from typing import Collection

from tweet_producer.domain.model.message import ProcessedMessage


class DatabaseMessageRepository(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def save_message(self, processed_message: ProcessedMessage) -> None: ...

    @abstractmethod
    def get_messages(self) -> Collection[ProcessedMessage]: ...
