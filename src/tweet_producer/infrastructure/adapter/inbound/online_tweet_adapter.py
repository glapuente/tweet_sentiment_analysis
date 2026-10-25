from tweet_producer.application.port.inbound.message_repository import MessageRepository
from typing import List
from tweet_producer.domain.model.message import ProcessedMessage, RawMessage


class OnlineTweetRepository(MessageRepository):
    def __init__(
        self,
    ):
        super().__init__()


    def fetch_messages(
        self,
        n_messages: int=None,
    ) -> List[ProcessedMessage]:
        #TODO: implement method for fetching tweets through X's API
        pass
