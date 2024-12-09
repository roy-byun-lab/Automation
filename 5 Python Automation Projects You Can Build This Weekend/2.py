"""
Social Media Post Scheduler
The following is an automation project that will enable you to schedule posts to Twitter at specific times.

What You’ll Need:
    1.Twitter Developer API (Access to your Twitter account)
    2.schedule Python library (For scheduling posts)
"""
import tweepy
import schedule
import time

# Twitter API authentication
auth = tweepy.OAuth1UserHandler(
    consumer_key="your_consumer_key",
    consumer_secret="your_consumer_secret",
    access_token="your_access_token",
    access_token_secret="your_access_token_secret"
)
api = tweepy.API(auth)

# Function to post a tweet
def post_tweet():
    tweet = "Automated tweet using Python! #PythonRocks #helloworld"
    api.update_status(tweet)
    print("Tweet posted!")

# Schedule the tweet to be posted at 9 AM every day
schedule.every().day.at("09:00").do(post_tweet)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)