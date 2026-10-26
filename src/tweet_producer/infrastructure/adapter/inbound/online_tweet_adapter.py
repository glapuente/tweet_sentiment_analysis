from collections.abc import Generator

from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.domain.model.message import ProcessedMessage


class OnlineTweetRepository(MessageRepository):
    def __init__(
        self,
    ):
        super().__init__()


    def fetch_messages(
        self,
        n_messages: float,
    ) -> Generator[ProcessedMessage]:
        #TODO: implement method for fetching tweets through X's API
        raise NotImplementedError
