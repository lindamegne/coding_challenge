*Linda Megne 07/10/2015*

Insight Data Engineering - Coding Challenge - Documentation
===========================================================

In this coding challenge, it has been asking to develop tools that would help analyze the community of Twitter users. we have implemented two features : 

- Calculate the total number of times each word has been tweeted.

- Calculate the median number of unique words per tweet. This one have been implemented by using an input file and by connected the code to an API. In the second case the median is calculated in live and updated when tweet messages come in
  

## Communication with the user

The program is writing in python on ubuntu 12.04. The version used is python 2.7. t
Make sure that all the libraries which have been imported in the program exist in the system before running the program. Those libraries are: 

- itertools

- subprocess

- Counter from collections

- split from re

- sys
 
 To excecute the program, user should:
 
 - open the command line
 - change directory to be in the folder where your program is
 - type te command: *bash run.sh*

## Program execution

There is a shell script file named run.sh in the folder that allow to exsecute 3 programs. 

First and second programs of the file are executed by using an input file named tweets.txt. Input file is a list of tweet messages. The first program, words_tweeted.py produce the total count for each word in the Input file and save them in the output file named ft1.txt. The second program, median_unique.py produce the median number of unique words per tweet and save tem to ft2.txt

The third program is connected to API named tweepy. It saves messages send by tweeted in live in a text file API_tweets.txt And uses those tweet to calculate the median. This median is updated as tweets come in and save in the file ft3.txt. The file contains all the median that have been calculated. 

##Program structure

###The program have four .py file:

*words_tweet.py file has 2 functions:*

init : initialization function.

count_words: this function creates a list of the words from input file tweets.txt and the number of time each word appears. It takes filename as parameter


* words_tweet.py file has 2 functions:*

init : initialization function.

Median_number: this function count the number of words in each tweet and store them in a list. Ten it uses that list to calculate the median of the word in tweets as tweets come in. It takes the input file in parameter and  return a list of median


*data_collection_tweepy.py has 3 function*

init : initialization function.

on_status: this function save data in a text file  It calculates the median of words in tweet When reach a number of tweets (the default number of tweet have been fixed at 10. It is possible to change it anytime), the program stops collections of data

on_error: Called when a non-200 status code is returned and print the status on screen

*print_features.py has 5 functions:*

init: initialization function.

print_words_to_screen: This function print list of the words from input file and the number of time each word appears to the command line screen. It takes the list of the words and the number of time each of them appears returned by count_words in parameter. It takes a second parameter used by an impoted function named lambda.

print_words_to_file : This function print the list of the words and how many time each word appear to the output file, It takes the list returned by count_words and the output file in parameter. It takes a third parameter used by an impoted function named lambda.

print_to_screen: This function print medians calculated to the command line screen. It takes the list on median returned by median_number in parameter

print_to_file : This function print medians calculated to the output file. It takes the list on median returned by median_number and the output file in parameter. 

### Input and output file

*Input file*

There is one input file tweet.txt where tweet messages are saved

*Output file*

There are four output file. 
- ft1.txt to save the words and the number of time each of them appear 
- ft2.txt to save median of unique word per tweet.
- ft3.txt to save median of unique word per tweet. This one is connected to API and the file is updated as tweet messages come in

## Example

is #bigdata finally the answer to end poverty? @lavanyarathnam http://ow.ly/o8gt3 #analytics
interview: xia wang, astrazeneca on #bigdata and the promise of effective healthcare #kdn http://ow.ly/ot2uj
big data is not just for big business. on how #bigdata is being deployed for small businesses: http://bddy.me/1bzukb3 @cxotodayalerts #smb
The first feature would produce the following total count for each word:

 #analytics                  1
 
 #bigdata                    3
 
 #kdn                        1
 
 #smb                        1
 
 @cxotodayalerts             1
 
 @lavanyarathnam             1
 
 and                         1
 
 answer                      1
 
 astrazeneca                 1
 
 being                       1
 
 big                         2
 
 business.                   1 
 
 businesses:                 1
 
 data                        1
 
 deployed                    1
 
 effective                   1
 
 end                         1
 
 finally                     1
 
 for                         2
 
 healthcare                  1
 
 how                         1
 
 http://bddy.me/1bzukb3      1
 
 http://ow.ly/o8gt3          1
 
 http://ow.ly/ot2uj          1
 
 interview:                  1
 
 is                          3
 
 just                        1
 
 not                         1
 
 of                          1
 
 on                          2
 
 poverty?                    1
 
 promise                     1
 
 small                       1
 
 the                         2
 
 to                          1
 
 wang,                       1
 
 xia                         1


For the second feature, the number of unique words in each tweet is 11, 14, and 17 (since the words 'is', 'big', and 'for' appear twice in the third tweet). This means that the set of unique words per tweet is {11} after the first tweet arrives, is {11, 14} after the second tweet arrives, and is {11, 14, 17} after all three tweets arrive. Thus, the second feature would produce the following output:

 11
 
 12.5
 
 14
 
