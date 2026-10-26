from tweet_producer.application.port.inbound.message_repository import MessageRepository


class TweetProducer:
    def __init__(
        self,
        message_repository: MessageRepository,
    ):
        self._message_repository = message_repository


    def produce_tweets(
        self,
        message_per_second: float,
    ) -> None:
        for row in self._message_repository.fetch_messages(message_per_second):
            print(row)


