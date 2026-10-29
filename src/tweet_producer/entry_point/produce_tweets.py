from os import getenv

from dotenv import load_dotenv

from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.application.use_cases.produce_tweets import TweetProducer
from tweet_producer.infrastructure.adapter.inbound.offline_tweet_adapter import (
    OfflineTweetRepository,
)
from tweet_producer.infrastructure.adapter.inbound.online_tweet_adapter import (
    OnlineTweetRepository,
)
from tweet_producer.infrastructure.adapter.outbound.kafka_message_repository import KafkaMessageRepository

if __name__ == "__main__":
    print("Producing tweets...")
    load_dotenv()

    tweet_repository: MessageRepository
    if bool(getenv("OFFLINE_MODE")):
        tweet_repository = OfflineTweetRepository(
            tweets_location=getenv(
                "TWEETS_LOCATION", "input_data/tweets/tweets_sample.csv"
            ),
        )
    else:
        tweet_repository = OnlineTweetRepository()

    tweet_consumer = TweetProducer(
        message_repository=tweet_repository,
        outbound_message_repository=KafkaMessageRepository(),
    )
    tweet_consumer.produce_tweets(float(getenv("MESSAGES_PER_SECOND", "5.0")))
