# Import the needed Libraries. Tweepy for Twitter Authentication
import tweepy
import csv

# Twitter Keys, Tokens and Secrets configuration for Twitter API Connection (Twitter Developer)
API_KEY = TWITTER_API_KEY
API_SECRET = TWITTER_API_SECRET
ACCESS_TOKEN = TWITTER_ACCESS_TOKEN
ACCESS_TOKEN_SECRET = TWITTER_ACCESS_TOKEN_SECRET

# Begin connection to Twitter with OAuth
a = tweepy.OAuthHandler(API_KEY,API_SECRET)
a.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
API = tweepy.API(a)

# Choose Twitter topic for Hashtag in Tweets
topic="#nuremberg"

# Filtering the results
tweets = tweepy.Cursor(API.search_tweets, q = topic, lang='en').items(20)
data=[[tweet.id_str,tweet.created_at,tweet.retweet_count,
tweet.text.encode("utf-8")] for tweet in tweets]

# Write filtered results in a csv document
with open('%s_tweets.csv' % topic, 'w') as f:
 writer = csv.writer(f)
 writer.writerow(["Id","Created_at","Retweet_count","Text"])
 writer.writerows(data)
