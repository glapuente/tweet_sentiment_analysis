from dotenv import load_dotenv
from os import getenv
from tweet_producer.application.use_cases.produce_tweets import TweetProducer
from tweet_producer.infrastructure.adapter.inbound.tweet_adapter import TweetRepository

if __name__ == '__main__':
    print("Producing tweets...")
    load_dotenv()

    tweet_consumer = TweetProducer(
        message_repository=TweetRepository(
            is_offline_mode=bool(getenv('OFFLINE_MODE')),
            tweets_location=getenv('TWEETS_LOCATION'),
        ),
    )
    tweet_consumer.produce_tweets()
