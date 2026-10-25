from tweet_producer.application.port.inbound.message_repository import MessageRepository
from typing import List
from tweet_producer.domain.model.message import ProcessedMessage, RawMessage
from faker import Faker
import pandas as pd


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
    ) -> List[ProcessedMessage]:

        print(self._tweets_location)

        tweet_chunk = pd.read_csv(
            filepath_or_buffer=self._tweets_location,
            chunksize=message_per_second,
            names=list(RawMessage.__annotations__.keys()),
        )
        print(tweet_chunk.to_string())

        #TODO: transform DataFrame before transforming it to JSON
        # print(tweet_chunk.to_json(orient="records"))


    @staticmethod
    def __add_fake_address(tweets: List[ProcessedMessage]) -> List[ProcessedMessage]:
        fake = Faker()
        for tweet in tweets:
            fake.address()



