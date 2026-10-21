from abc import abstractmethod, ABC
from typing import List
from tweet_producer.domain.model.message import ProcessedMessage


class MessageRepository(ABC):
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret


    @abstractmethod
    def fetch_messages(
        self,
    ) -> List[ProcessedMessage]:
        ...