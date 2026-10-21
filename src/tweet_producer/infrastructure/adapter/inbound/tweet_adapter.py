from tweet_producer.application.port.inbound.message_repository import MessageRepository
from typing import List
from tweet_producer.domain.model.message import ProcessedMessage, RawMessage
from faker import Faker
import pandas as pd


class TweetRepository(MessageRepository):
    def __init__(
        self,
        is_offline_mode: bool,
        tweets_location: str=None,
    ):
        super().__init__(is_offline_mode, tweets_location)


    def fetch_messages(
        self,
        n_messages: int=None,
    ) -> List[ProcessedMessage]:

        print(self._is_offline_mode)
        print(self._tweets_location)

        if self._is_offline_mode:
            tweet_chunk = pd.read_csv(
                filepath_or_buffer=self._tweets_location,
                chunksize=n_messages,
                names=list(RawMessage.__annotations__.keys()),
            )
            #TODO: transform DataFrame before transforming it to JSON
            print(tweet_chunk.to_json(orient="records"))
        else:
            #TODO: fetch messages online
            pass

    @staticmethod
    def __add_fake_address(tweets: List[ProcessedMessage]) -> List[ProcessedMessage]:
        fake = Faker()
        for tweet in tweets:
            fake.address()



