import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def fetch_reddit_data(keywords, limit=100):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    posts = []
    for keyword in keywords:
        for submission in reddit.subreddit("all").search(keyword, limit=limit):
            posts.append({
                "source": "reddit",
                "timestamp": submission.created_utc,
                "content": submission.title + " " + submission.selftext,
                "keyword": keyword
            })
    return posts
