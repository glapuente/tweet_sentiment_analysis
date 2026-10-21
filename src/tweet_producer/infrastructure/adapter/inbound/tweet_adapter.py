from typing import List
from tweet_producer.application.port.inbound.message_repository import MessageRepository


class TweetRepository(MessageRepository):

    def __init__(self):
        self._qwe = 1


    def fetch_messages(
        self,
    ):
        pass



