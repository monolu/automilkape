import tweepy
import time
import random
import threading
from threading import Thread

consumer_key = 'Lrmr9NQiyj6oerjxGwFCH3M8s'
consumer_secret = 'hl720f1416YINPUT9bHQ19B5YcmWxOr2puisqnyBeXQI4hncrx'
access_token = '1083981821535227904-mhUKjPR5cVetVEDUSbGS5gWWycOGJ3'
access_token_secret = 'pLE0TwK1MqUi33iUJ0ICmWtUKDsu3nPXWIAFGEUrATdY9'

#authorize for twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#establish rnn
from textgenrnn import textgenrnn
t = textgenrnn('ApeMiIk_twitter_weights.hdf5')

#different values for the temperature of the generated tweet
templist = [0.2, 0.5, 1.0]

#tweets a randomly generated phrase from the rnn every 6 hours
def auto_tweet():
    temp1 = random.choice(templist)
    to_tweet = ''.join(t.generate(n=1, temperature=temp1, return_as_list=True))
    str1 = ''.join(to_tweet)
    api.update_status(status = str1)
    print ('Tweeted ' + str1)

        
#automatically responds to tweets bot is tagged in
def auto_reply():
    while True:
        #generate the phrase
        temp2 = random.choice(templist)
        to_reply = ''.join(t.generate(n=1, temperature=temp2, return_as_list=True))
        str2 = ''.join(to_reply)

        #find latest tweet on own timeline, used to get tweet ID so the bot can't reply to tweets older than its latest tweet
        for latest in tweepy.Cursor(api.user_timeline, id = "ApeAutomated").items(1):
            latest_tweet = latest.id_str

        #the loop for posting the reply, keyphrases separated by OR
        for tweet in tweepy.Cursor(api.search, q='@ApeAutomated wisdom OR @ApeAutomated ape OR @ApeAutomated monkey OR @ApeAutomated ? OR @ApeAutomated love',since_id=latest_tweet).items(5):
            print ("Found tweet by:@" + tweet.user.screen_name)
            api.update_status(status = '@' + tweet.user.screen_name + ' ' + str2, in_reply_to_status_id = tweet.id_str)
            print ('responded to @' + tweet.user.screen_name)

        time.sleep(10)

auto_tweet()
auto_reply()

# if __name__ == '__main__':
#     Thread(target = auto_tweet).start()
#     Thread(target = auto_reply).start()