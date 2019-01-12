import tweepy
import time

consumer_key = 'Lrmr9NQiyj6oerjxGwFCH3M8s'
consumer_secret = 'hl720f1416YINPUT9bHQ19B5YcmWxOr2puisqnyBeXQI4hncrx'
access_token = '1083981821535227904-mhUKjPR5cVetVEDUSbGS5gWWycOGJ3'
access_token_secret = 'pLE0TwK1MqUi33iUJ0ICmWtUKDsu3nPXWIAFGEUrATdY9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

from textgenrnn import textgenrnn
t = textgenrnn('textgenrnn_weights.hdf5')

to_tweet = ''.join(t.generate(n=1, temperature=1.0, return_as_list=True))
str1 = ''.join(to_tweet)

for tweet in tweepy.Cursor(api.search, q='@ApeAutomated', lang = 'en').items(1):
    try:
        print ("Found tweet by:@" + tweet.user.screen_name)
        api.update_status(status = '@' + tweet.user.screen_name + ' ' + str1, in_reply_to_status_id = tweet.id_str)
        print ('responded to @' + tweet.user.screen_name)
        
    except tweepy.TweepError as e:
        print(e.reason)
        time.sleep(3)
        continue
    except tweepy.RateLimitError:
        time.sleep(15*60)
    except StopIteration:
        break

# while True:
#     api.update_status(status = str1)
#     time.sleep(21600)

