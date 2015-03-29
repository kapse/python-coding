""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 07 18:36:54 2015

@author: VAIBHAV
"""

"""  code to calculate the sentiment score of each tweet text
in the raw tweet le "CrimeReport.txt" and print out the sen-
timent score for each tweet. """

import sys;
reload(sys);
sys.setdefaultencoding("utf8")
import json
import os
from pattern.en import sentiment, positive
def main():

    tweets = []
    lines = open('CrimeReport.txt').readlines()
    for line in lines:
        tweet = json.loads(line)
        tweets.append(tweet)

    ntweets = []
    ptweets = []

    for tweet in tweets:
        tweet_text = tweet['text']
        tweet_assment = sentiment(tweet_text)
        
        print 'TWEET TEXT: {0}'.format(tweet_text)
        print 'SENTIMENT SCORE: {0}'.format(tweet_assment)

       
if __name__ == '__main__':
    main()


