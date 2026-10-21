from typing import List
from tweet_producer.application.port.inbound.message_repository import MessageRepository


class TweetProducer:
    def __init__(
        self,
        message_repository: MessageRepository,
    ):
        self._message_repository = message_repository


    def produce_tweets(
        self,
    ) -> None:
        self._message_repository.fetch_messages()

