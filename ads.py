#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:48:41 2019

@author: rgukt
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
[fs,y]=wav.read("/home/rgukt/Desktop/v1.wav")
fs=float(fs)
fs2=2*fs
print(fs,len(y),y)
t1=np.arange(0,len(y)/fs,1.0/fs)
t2=np.arange(0,len(y)/fs2,1.0/fs)
#print(y)
a1=plt.subplot(211)
a1.plot(t1,y)
a2=plt.subplot(212)
a2.plot(t2,y)
plt.show()

#wav.write('home/rgukt/Desktop/v1.wav',2*fs,y)
