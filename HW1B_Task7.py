""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """


""" Read the tweets from the le "CrimeReport.txt" and print the
id for each tweet.. """


import json;
def main():
    for line in open('CrimeReport.txt').readlines():
        tweet = json.loads(line)
        if tweet['id']:
            print (tweet['id'])
   
if __name__ == '__main__':
    main()