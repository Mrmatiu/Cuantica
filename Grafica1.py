#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:32:58 2019

@author: matthew
"""

import numpy as np
import pylab

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
pi = 3.1416

def planck(freq, T):
    return 8.0*h*freq**3/(c**2) *np.exp(h*freq/(k*T))

frequency = np. linspace (0.1, 10**15, 10000)
T = np.array([100., 500., 1000., 1500., 2000.])

pfuncs = planck (frequency, T[:,None] )

for pfunc in pfuncs:
    pylab.plot(frequency, pfunc)
pylab.show()



# intensity at 4000K, 5000K, 6000K, 7000K
#intensity100 = planck(frequency, 100.)
#intensity500 = planck(frequency, 500.)
#intensity1000 = planck(frequency, 1000.)
#intensity1500 = planck(frequency, 1500.)
#intensity2000 = planck(frequency, 2000.)

#plt.plot(frequency*1e9, intensity100, 'r-') 
# plot intensity100 versus wavelength in nm as a red line
#plt.plot(frequency*1e9, intensity500, 'g-') # 500K green line
#plt.plot(frequency*1e9, intensity1000, 'b-') # 1000K blue line
#plt.plot(frequency*1e9, intensity1500, 'k-') # 1500K black line
#plt.plot(frequency*1e9, intensity2000, 'y-') # 2000K yellow line

# show the plot
#plt.show()