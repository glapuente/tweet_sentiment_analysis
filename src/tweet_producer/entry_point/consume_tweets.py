from os import getenv

from dotenv import load_dotenv
from pyspark.sql import SparkSession

from tweet_producer.application.port.inbound.message_repository import MessageRepository
from tweet_producer.application.use_cases.consume_tweets import TweetConsumer
from tweet_producer.infrastructure.adapter.inbound.kafka_message_consumer import (
    SparkKafkaMessageConsumer,
)
from tweet_producer.infrastructure.adapter.outbound.postgres_message_repository import PostgresMessageRepository
from tweet_producer.infrastructure.config.kafka_configuration import KafkaConfiguration
from tweet_producer.infrastructure.config.postgres_configuration import PostgresConfiguration


def tweet_consumer() -> None:
    print("Consuming tweets...")
    load_dotenv()

    tweet_repository: MessageRepository = SparkKafkaMessageConsumer(
        kafka_topic=getenv("KAFKA_TOPIC", "test-topic"),
        kafka_configuration=KafkaConfiguration(
            kafka_host=getenv("KAFKA_HOST", "localhost"),
            kafka_port=int(getenv("KAFKA_PORT", "9092")),
        ),
        spark_session=(
            SparkSession.builder.master("local[*]")
            .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true")
            .config(
                "spark.jars.packages",
                "org.apache.spark:spark-sql-kafka-0-10_2.13:4.3.0,"
                "org.postgresql:postgresql:42.7.8"
            )
            .appName(getenv("APP_NAME", "TweetProducer"))
            .getOrCreate()
        ),
        database_message_repository=PostgresMessageRepository(
            postgres_configuration=PostgresConfiguration(
                postgres_db=getenv("POSTGRES_DB", "database"),
                postgres_table_name=getenv("POSTGRES_TABLE_NAME", "table_name"),
                postgres_host=getenv("POSTGRES_HOST", "localhost"),
                postgres_user=getenv("POSTGRES_USER", "user"),
                postgres_password=getenv("POSTGRES_PASSWORD", ""),
                postgres_port=int(getenv("POSTGRES_PORT", "5432")),
            )
        ),
    )

    message_consumer = TweetConsumer(
        message_repository=tweet_repository,
    )
    message_consumer.consume_tweets(float(getenv("MESSAGES_PER_SECOND", "5.0")))


if __name__ == "__main__":
    tweet_consumer()
