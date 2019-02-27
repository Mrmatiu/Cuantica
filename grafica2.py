#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:32:58 2019

@author: matthew
"""

import numpy as np
import pylab

T = np.array([100, 500, 1000, 1500, 2000])
v = np. linspace (0.1, 10**15, 10000)

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
pi = 3.1416
Y = h*v/k

def planck(freq, T):
    a = 8.0*pi*h*freq**3
    densidad = a/ ( (c**3) * (np.exp(Y/T) - 1.0) )
    return densidad

pfuncs = planck(v, T[:,None] )

plt.ylabel(' Densidad(v)')
plt.xlabel('frecuencia (Hz)')
plt.title('Densidad de energia de un cuerpo negro')
plt.grid(True)

for pfunc in pfuncs:
    pylab.plot(v,pfunc)
pylab.show()

