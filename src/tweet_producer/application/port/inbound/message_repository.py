from abc import abstractmethod, ABC
from typing import List
from tweet_producer.domain.model.message import ProcessedMessage


class MessageRepository(ABC):
    def __init__(
        self,
        is_offline_mode: bool,
        tweets_location: str = None,
    ):
        self._is_offline_mode = is_offline_mode
        if is_offline_mode:
            self._tweets_location = tweets_location


    @abstractmethod
    def fetch_messages(
        self,
    ) -> List[ProcessedMessage]:
        ...