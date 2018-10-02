from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)

if name__== "__main__":
    listener = StdOutListener()
    auth =  OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    
