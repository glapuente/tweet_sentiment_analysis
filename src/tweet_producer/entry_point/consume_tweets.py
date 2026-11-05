from os import getenv

from dotenv import load_dotenv

from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.application.use_cases.consume_tweets import TweetConsumer
from tweet_producer.application.use_cases.produce_tweets import TweetProducer
from tweet_producer.infrastructure.adapter.inbound.kafka_message_consumer import SparkKafkaMessageConsumer
from tweet_producer.infrastructure.adapter.inbound.offline_tweet_adapter import (
    OfflineTweetRepository,
)
from tweet_producer.infrastructure.adapter.inbound.online_tweet_adapter import (
    OnlineTweetRepository,
)
from tweet_producer.infrastructure.adapter.outbound.kafka_message_producer import (
    KafkaMessageProducer,
)
from tweet_producer.infrastructure.config.kafka_configuration import KafkaConfiguration


def tweet_consumer():
    print("Consuming tweets...")
    load_dotenv()

    tweet_repository: MessageRepository
    if getenv("OFFLINE_MODE") == 'true':
        tweet_repository = OfflineTweetRepository(
            tweets_location=getenv(
                "TWEETS_LOCATION", "input_data/tweets/tweets_sample.csv"
            ),
        )
    else:
        from pyspark.sql import SparkSession

        import os
        import sys

        #TODO: check how I could solve this..
        os.environ["PYSPARK_PYTHON"] = sys.executable
        os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


        tweet_repository = SparkKafkaMessageConsumer(
            kafka_topic=getenv("KAFKA_TOPIC", "test-topic"),
            kafka_configuration=KafkaConfiguration(
                kafka_host=getenv("KAFKA_HOST", "localhost"),
                kafka_port=int(getenv("KAFKA_PORT", "9092")),
            ),
            spark_session=(
                SparkSession.builder
                .master("local[*]")
                .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true")
                .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:4.3.0")
                .appName(getenv("APP_NAME", "TweetProducer"))
                .getOrCreate()
            ),
        )

    message_consumer = TweetConsumer(
        message_repository=tweet_repository,
        # outbound_message_repository=KafkaMessageProducer(),
    )
    message_consumer.consume_tweets(float(getenv("MESSAGES_PER_SECOND", "5.0")))


if __name__ == "__main__":
    tweet_consumer()
