""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """


""" File operations
INPUT :CrimeReport.txt: in this le, each line is a raw tweet json format.
output-folder: where new results will be stored
REQUIREMENT: read tweets and separate these tweets in to groups
based on the specic hours (Mon-Day-Year-Hour). The tweets related
to a specic hour will be stored in a separate le in the folder "output-
folder" with the le name "Mon-Day-Year-Hour.txt"
OUTPUT: new les generated and stored in the folder "output-folder".
Each le stores the tweets related to a specic hour. """

import datetime
import json
import os
def main():
    dir_name = 'output-folder'
    tw = []
    lines = open('CrimeReport.txt').readlines()
    for ln in lines:
        tweet = json.loads(ln)
        tw.append(tweet)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)    
    for tweet in tw:  
        ts = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        yr  = ts.year
        mth = ts.month
        day   = ts.day
        hr  = ts.hour
        fnm = '%s-%s-%s-%s.txt' % (mth, day, yr, hr)      
        with open(os.path.join(dir_name, fnm), 'a') as f:
            f.write(json.dumps(tweet) + '\n')

if __name__ == '__main__':
    main()

