#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:18:40 2019

@author: matthew
"""

import matplotlib.pyplot as plt
import numpy as np


#Primero definiremos la ecuacion para obtener el factor de Lorentz
def FactorLorentz(rango):
    return (1/(1-(rango)**2)**(1/2))
vecfunc = np.vectorize(FactorLorentz)

#Definimos un arreglo de 1000 valores que se asignaran a la ecuacion definida, estos iran de 0-1.
arreglo = np.arange(0.0,1.0,0.001,float)

#Vectorizamos nuestra ecuacion para tener las mismas dimensiones que el arreglo
F = vecfunc(arreglo)

#Imprimimos nuestra grafica
plt.plot(arreglo,F, 'r')
plt.ylabel(' Factor de Lorentz')
plt.xlabel('Velocidad (v/c)')
plt.grid(True)
plt.show()
            
