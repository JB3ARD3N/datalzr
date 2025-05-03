import tweepy
from config import TWITTER_BEARER_TOKEN

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def fetch_twitter_data(keywords, limit=10):
    tweets = []
    for keyword in keywords:
        response = client.search_recent_tweets(query=keyword, max_results=limit)
        for tweet in response.data or []:
            tweets.append({
                "source": "twitter",
                "timestamp": tweet.created_at.timestamp(),
                "content": tweet.text,
                "keyword": keyword
            })
    return tweets
