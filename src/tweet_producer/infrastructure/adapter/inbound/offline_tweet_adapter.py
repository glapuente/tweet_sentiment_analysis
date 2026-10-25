from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.domain.model.message import ProcessedMessage, RawMessage
from faker import Faker
import csv
import time


class OfflineTweetRepository(MessageRepository):
    def __init__(
        self,
        tweets_location: str,
    ):
        super().__init__()
        self._tweets_location = tweets_location


    def fetch_messages(
        self,
        message_per_second: int=None,
    ) -> ProcessedMessage:
        with open(self._tweets_location, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                raw_message = RawMessage(*row)
                processed_message = self.__add_fake_address(raw_message)
                yield processed_message
                time.sleep(message_per_second)


    @staticmethod
    def __add_fake_address(raw_tweet: RawMessage) -> ProcessedMessage:
        fake = Faker()
        return ProcessedMessage(
            raw_tweet.username,
            raw_tweet.message_text,
            raw_tweet.published_at,
            fake.address(),
        )



