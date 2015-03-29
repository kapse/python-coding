""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 18:36:54 2015

@author: VAIBHAV
"""
"""  City level geocoding in tweets """

import sys;
reload(sys);
sys.setdefaultencoding("utf8")

import json
import os
import LocationResolver

def main():

    rs = LocationResolver.LocationResolver()
    ts = []
    ls = open('CrimeReport.txt').readlines()
    for line in ls:
        t = json.loads(line)
        ts.append(t)
    
    for t in ts:
        print t['id'] 
        lc = rs.resolveLocationFromTweet(t)
        if lc!=None:
            print lc.getDisplayString()
        else:
            print 'None'

if __name__ == '__main__':
    main()

