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
from tweet_producer.infrastructure.adapter.outbound.kafka_message_repository import (
    KafkaMessageRepository,
)
from tweet_producer.infrastructure.config.kafka_configuration import KafkaConfiguration


def tweet_producer():
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
        outbound_message_repository=KafkaMessageRepository(
            kafka_topic=getenv("KAFKA_TOPIC", "test-topic"),
            kafka_configuration=KafkaConfiguration(
                kafka_host=getenv("KAFKA_HOST", "localhost"),
                kafka_port=int(getenv("KAFKA_PORT", "9092")),
            ),
        ),
    )
    tweet_consumer.produce_tweets(float(getenv("MESSAGES_PER_SECOND", "5.0")))


if __name__ == "__main__":
    tweet_producer()
