#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 00:51:18 2020

@author: vineethmurukuti
"""

import pandas as pd
import numpy as np
import copy
from datetime import date
from scipy.signal import argrelextrema

columnstr='Timestamp,ISO Date,packages,processes,screenshot,scriptOutput,connected,hasRebooted,isOffline,isOnline,cpuLoad,cpuTemp,cpuTempMax,fs1Use,fs2Use,fs3Use,fs4Use,fs5Use,fs6Use,fs7Use,fsRx,fsTx,fsWx,memActive,memFree,memTotal,memUse,memUsed,net1Rx,net1Tx,processCount,uptime,wifiLevel,wifiQuality,scriptStatusId,status'
columns = columnstr.split(',')


#Read in the report
df = pd.read_csv('SampleInput.csv',sep='\t')
ua = np.array(df)

#Calculate days of data
start = copy.deepcopy(ua[0][0])
finish = copy.deepcopy(ua[len(ua) - 1][0])

starttime = start.split(',')[1]
finishtime = finish.split(',')[1]

date1 = starttime.split('T',1)
date2 = finishtime.split('T',1)
date1array= date1[0].split('-')
date2array= date2[0].split('-')

date1array = [int(i) for i in date1array] 
date2array = [int(i) for i in date2array] 


f_date = date(date1array[0], date1array[1], date1array[2])
l_date = date(date2array[0], date2array[1], date2array[2])




#final daycount
delta = l_date - f_date

#max possible uptime in seconds as a float
maxuptime= delta.total_seconds()


#flatten main array to 1D array of strings
mainarray = ua.flatten()


#array of only nonblank uptime values
utarr = []
for x in mainarray:
    if x.split(',')[31]!='':
        utarr.append(int(x.split(',')[31]))
        
#np formatted nonblank uptime vals
finalvals = np.array(utarr)
localmaxima= argrelextrema(finalvals, np.greater)
actualuptime = 0
for ind in localmaxima[0]:
    actualuptime += finalvals[ind]
    
actualuptime -= finalvals[0]
print(finalvals[0])
maxuptime+=(60*60*24)
percentuptime = float(100*(actualuptime/maxuptime))

print("From the start date "+date1[0]+ " to the end date of " +date2[0] + ", This door was up with or without an internet connection for " +str(round(percentuptime,4)) +" percent of a total "+str(delta).split(',')[0]) 


#Uptime With Internet 

#Grabbing only offline and online events 

#offonevents = []
#for x1 in mainarr 





















