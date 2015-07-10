"""
Author: Linda MEGNE
Email: lindamegne@gmail.com
Slidell, 07/10/2015
"""

import itertools
import numpy
from collections import Counter
from re import split
import sys
from print_features import output_print


class count_words_dict:


    """ Give list of words use in tweet messages and number of time each words appear """

    def __init__(self):
        """
            Function: init
            ---------------
            Initialize  global parameter
        """
        self.dict_words = {}
        
    def count_words(self,file_name):
        """
            Function: count_words
            ---------------------
            
            file_name: text file that contains tweet messages.
            
            return a dictionary of word in the input file with te number of time each word appear
            
        """
        
        file_object = open(file_name,"r")
        tweets = []
        for line in file_object:
            unique_words_per_tweet = (line.rstrip().split(" "))
            tweets.append(unique_words_per_tweet)
        file_object.close()
        tweeted_words = list(itertools.chain.from_iterable(tweets))
        self.unique_words = dict(Counter((tweeted_words)))
        return self.unique_words


input_file = sys.argv[1]
output_file = sys.argv[2]

out = output_print()
word = count_words_dict()

word_dict = word.count_words(input_file)

out.print_words_to_screen(word_dict, is_reverse = False)
out.print_words_to_file(word_dict, output_file, is_reverse = False)
