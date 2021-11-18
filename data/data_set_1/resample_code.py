# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import IPython as IP
IP.get_ipython().magic('reset -sf')

import numpy as np
import scipy as sp
import pandas as pd
from scipy import fftpack, signal # have to add 
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn as sk
import time as time
from sklearn import linear_model
from sklearn import pipeline
from sklearn import datasets
from sklearn import multiclass

import json as json

plt.close('all')




#%% load and resample the data to a set sample rate. 


D = np.loadtxt('accel_1.csv',skiprows=2,delimiter=',')
start = 300
stop = 1000
tt = D[start:stop,0]
acc = D[start:stop,1:6]

sample_rate = 500000 # set the new sample rate in samples / sec
tt_new = np.arange(tt[0],tt[-1],1/sample_rate)



acc_new = np.zeros((tt_new.shape[0],6))
for i in range(5):
    f = sp.interpolate.interp1d(tt, acc[:,i], kind='linear')
    acc_new[:,i] = f(tt_new)

    plt.figure()
    plt.plot(tt,acc[:,i],label='data')
    plt.plot(tt_new,acc_new[:,i],'--o',label = 'resampled')
             
    plt.legend()

D_out = np.hstack((np.expand_dims(tt_new,axis=1),acc_new))

# save the data with headers
np.savetxt('accel_1_custom.csv', D_out, header='time, accel 1, accel 2, accel 3, accel 4, accel top, accel bottom \ntime - seconds (computed after test), deacceleration - kg, deacceleration - kg, deacceleration - kg, deacceleration - kg, deacceleration - kg, deacceleration - kg', comments = '',delimiter = ',')



















































