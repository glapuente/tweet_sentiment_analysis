from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.application.port.outbound.outbound_message_repository import OutboundMessageRepository


class TweetProducer:
    def __init__(
        self,
        message_repository: MessageRepository,
        outbound_message_repository: OutboundMessageRepository,
    ):
        self._message_repository = message_repository
        self._outbound_message_repository = outbound_message_repository

    def produce_tweets(
        self,
        message_per_second: float,
    ) -> None:
        for message in self._message_repository.fetch_messages(message_per_second):
            self._outbound_message_repository.append_message(processed_message=message)
            print(message)
