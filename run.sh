#!/usr/bin/env bash


# I'll execute my programs, with the input directory tweet_input and output the files in the directory tweet_output
#python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
#python ./src/median_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt

python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
python ./src/median_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt
python ./src/data_collection_tweepy.py ./tweet_output/API_tweets.txt ./tweet_output/ft3.txt
