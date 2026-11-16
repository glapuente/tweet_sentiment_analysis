import csv
import time
from collections.abc import Generator
from datetime import datetime

from faker import Faker

from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.domain.model.message import ProcessedMessage, RawMessage, Location


class OfflineTweetRepository(MessageRepository):
    def __init__(
        self,
        tweets_location: str,
    ):
        super().__init__()
        self._tweets_location = tweets_location

    def fetch_messages(
        self,
        message_per_second: float,
    ) -> Generator[ProcessedMessage]:
        with open(
            self._tweets_location, mode="r", newline="", encoding="utf-8"
        ) as file:
            reader = csv.reader(file)
            for row in reader:
                raw_message = RawMessage(
                    sentiment_value=int(row[0]),
                    message_id=int(row[1]),
                    published_at=datetime.strptime(row[2], "%a %b %d %H:%M:%S %Z %Y"),
                    query=str(row[3]),
                    username=str(row[4]),
                    message_text=str(row[5]),
                )
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
            Location(*fake.location_on_land()),
        )
