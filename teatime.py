import automationhat
import time
import random
import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

# your Twitter access codes go here
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
        # the red light is output one on the Automation pHat,
        # amber is output two, and green is three.
        # The buzzer is connected to the relay
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
    # Adds a random number to the end of the tweet to avoid duplicate tweet errors
    # Replace the unsername and tweet text here with something appropriate for you  
    j = random.getrandbits(8)  
    api.update_status('@USERNAMEYOUWANTTOALERT tweet_you_want_to_send ',j)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

# flash and beep to confirm start up
for i in range(3):
    automationhat.output.one.on()
    time.sleep(0.2)
    automationhat.output.one.off()
    automationhat.output.two.on()
    time.sleep(0.2)
    automationhat.output.two.off()
    automationhat.output.three.on()
    time.sleep(0.2)
    automationhat.output.three.off()
automationhat.relay.one.on()
time.sleep(0.2)
automationhat.relay.one.off()
l = random.getrandbits(6)
# Edit the Twitter account you want to alert and the text you'll send them
api.update_status('@USERNAMEYOUWANTTOALERT wake_up_notification_tweet ',l)

twitterstream = Stream(auth, listener())
twitterstream.filter(track=['#teatimejack'])
