import matplotlib.pyplot as plt
import numpy as np

h = 6.626e-34
e = 1.602e-34
w = 3.700e-19

#Primero definiremos la ecuacion para obtener el factor de Lorentz
def Frenamiento(freq):
  return (((h*freq)-w)/e)

#Definimos un arreglo de n valores que se asignaran a la ecuacion definida.
arreglo = np.arange(1e+14, 20e+14,1e+10, float)

#Vectorizamos nuestra funcion para obtener las dimensiones del arreglo
vecfunc = np.vectorize(Frenamiento)

#Vectorizamos nuestra ecuacion para tener las mismas dimensiones que el arreglo
F = vecfunc(arreglo)

#Imprimimos nuestra grafica
plt.plot(arreglo,F, 'r')
plt.ylabel(' Potencial de frenado (V)')
plt.xlabel('Frecuencia (10^14/seg)')
plt.grid(True)
plt.show()


