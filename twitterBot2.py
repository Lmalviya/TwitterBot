import tweepy
import time 

auth = tweepy.OAuthHandler("API key", "API secret key:")
auth.set_access_token("Access token", "Access token secret")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'python'
nrTweets = 800      #number of like post in one attempt if not close the process

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
