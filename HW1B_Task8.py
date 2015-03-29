""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """

""" Filter tweets
INPUT: "CrimeReport.txt"
OUTPUT: a le "output.txt" that stores the 10 most recent tweets """

import datetime
import json
def main():
   tweets = []
   for line in open("CrimeReport.txt").readlines():
       tweet=json.loads(line)
       
       if tweet['created_at']:
           print tweet
           tweets.append(tweet)
           datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
           sorted_tweets = sorted(tweets, key = lambda tweet: datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
           f = open('output.txt', 'w') 
           for tweet in sorted_tweets[-10:]:  
               f.write(json.dumps(tweet) + '\n')
               
           f.close()


if __name__ == '__main__':
	main()