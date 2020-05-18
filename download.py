import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import time
from keys import*

consumer_key = cKey
consumer_secret = cSecret
access_token = aToken
access_secret = aSecret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)



class MyListener(StreamListener):
	def __init__(self, time_limit=60):
		self.start_time = time.time()
		self.time_limit = time_limit
		self.output = open ('Tweets.json','a')
		super(MyListener,self).__init__()
	def on_data(self, data):
		if (time.time()-self.start_time) < self.time_limit:
			self.output.write(data)
			return True
		else:
			self.output.close()
			return False
	def on_error(self,status):
		print status
		return True

twitter_stream = Stream(auth, MyListener(time_limit=(10*60)))
twitter_stream.sample()
#twitter_stream.filter(track=['COVID19'])
