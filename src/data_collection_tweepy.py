"""
Author: Linda MEGNE
Email: lindamegne@gmail.com
Slidell, 07/10/2015
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import sys
import itertools
import numpy
from collections import Counter
from re import split
from print_features import output_print


#consumer key, consumer secret, access token, access secret.
ckey="Kg2kuisHei7VRHrB8IoKxEwqI"
csecret="Zm03UjhUTR60c3gAmVcxPPUOjfKF0bG53O6VjxIbeirItesOcL"
atoken="2391531949-RInQxieab8Tf3O6AuxY6f3MB6bUK8oQs0fhIlx8"
asecret="jIVmxfxcXAFsu0xeIuKdLKkj5gXpJvDyxdOJljnAwtAQt"


class listener(StreamListener):
    """
        Get tweet message using API tweepy.user have to be connected on his tweeter account 
        Messages are then save in a text file.
        In same time, the class calculates the median of unique words per tweet.
        The median is then update as tweet come in. All the tweet are save in a text file
    """

    def __init__(self, api=None):
        """
            Function: init
            --------------
            Initialize  global parameter

        """
        super(listener, self).__init__()
        self.number_tweets = 0                  # Initialize number of tweets to 0
        self.max_tweets = 10                    # Maximum number of tweet. Over this number the program stops
        self.med_words_list =[]                 # List of median of all tweet collected
        self.med_words = []                     # Ledian of unique words in one tweet
        self.out = output_print()

    def on_status(self, status):
        """
            Function: on_status
            ---------------
            init initialize parameters.

            this function save data in a text file.
            It calculates the median of words in tweet
            When reach a number of tweets, the program stops collections of data
        """
        tweet_file = sys.argv[1]                # text file to save tweet messages in
        med_file = sys.argv[2]                  # text file to save median in

        data = status.text.encode("utf-8")      # tweet messages
        open(tweet_file, "a").write(data)
        open(tweet_file, "a").write("\n")

        unique_words_per_tweet = sorted(set(data.rstrip().split(" ")))
        number_words_per_tweet = len(Counter((unique_words_per_tweet)))
        self.med_words.append(number_words_per_tweet)
        self.med_words_list.append(numpy.median(numpy.array(self.med_words)))
        self.out.print_med_to_screen(self.med_words_list)
        self.out.print_med_to_file(self.med_words_list, med_file)

        self.number_tweets += 1
        if self.number_tweets < self.max_tweets:
            return True
        else:
            return False
        open(tweet_file, "a").close()

    def on_error(self, status):
        """ Called when a non-200 status code is returned """
        print status
        return True


l = listener()
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, l)
twitterStream.filter(track=["bigdata"])