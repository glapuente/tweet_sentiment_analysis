from tweet_producer.application.port.inbound.message_repository import MessageRepository
from typing import List
from tweet_producer.domain.model.message import Message

class TweetRepository(MessageRepository):

    def __init__(self):
        self._qwe = 1


    def fetch_messages(
        self,
    ) -> List[Message]:
        pass



