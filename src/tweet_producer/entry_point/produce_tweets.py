from dotenv import load_dotenv
from os import getenv
from tweet_producer.application.use_cases.produce_tweets import TweetProducer
from tweet_producer.infrastructure.adapter.inbound.offline_tweet_adapter import OfflineTweetRepository
from tweet_producer.infrastructure.adapter.inbound.online_tweet_adapter import OnlineTweetRepository

if __name__ == '__main__':
    print("Producing tweets...")
    load_dotenv()

    if bool(getenv('OFFLINE_MODE')):
        tweet_repository= OfflineTweetRepository(
            tweets_location=getenv('TWEETS_LOCATION'),
        )
    else:
        tweet_repository= OnlineTweetRepository()  #TODO: create class for this


    tweet_consumer = TweetProducer(
        message_repository=tweet_repository,
    )
    tweet_consumer.produce_tweets()
