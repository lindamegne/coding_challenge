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



class median_unique:

    """ calculate the median of unique words per tweet and update the median as tweet comme in """

    def __init__(self):
        """
            Function: init
            ---------------
            Initialize  global parameter
        """
        self.median_number_list = []
    
    def median_number(self, file_name):
        """
            Function: median_number
            -----------------------

            file_name: input file are tweets and are used to calculate median

            return a list of medians. It counts the unique words per tweet 
        """

        file_object = open(file_name, "r")
        number_word_list = []
        for line in file_object:
            unique_words_per_tweet = sorted(set(line.rstrip().split(" ")))
            number_word_list.append(len(Counter((unique_words_per_tweet))))
            self.median_number_list.append(numpy.median(numpy.array(number_word_list)))
        return  self.median_number_list

input_file = sys.argv[1]
output_file = sys.argv[2]

out = output_print()
med = median_unique()

med_list = med.median_number(input_file)

out.print_med_to_screen(med_list)
out.print_med_to_file(med_list, output_file)
