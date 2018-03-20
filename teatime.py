import automationhat
import time
import random
import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'YOURCONSUMERKEY'
csecret = 'YOURCONSUMERSECRET'
atoken = 'YOURACCESSTOKEN'
asecret = 'YOURACCESSSECRET'

class listener(StreamListener):
    def on_data(self, data):
        teatime()
        return True

def teatime():
    for i in range(5):
        automationhat.output.three.on()
        time.sleep(0.5)
        automationhat.output.three.off()
        automationhat.output.two.on()
        time.sleep(0.5)
        automationhat.output.two.off()
        automationhat.output.one.on()
        automationhat.relay.one.on()
        time.sleep(0.5)
        automationhat.output.one.off()
        automationhat.relay.one.off()
        time.sleep(0.5)
    j = random.getrandbits(8)
    api.update_status('@USERNAMEYOUWANTTOALERT tweet you want to send ',j)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
twitterstream = Stream(auth, listener())
twitterstream.filter(track=['#teatimejack'])
