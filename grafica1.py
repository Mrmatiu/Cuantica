import matplotlib.pyplot as plt
import numpy as np
a= 1
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
pi = 3.1416

def planck(freq, T):
    a = 8.0*h*freq**3
    b = h*freq/(k*T)
    densidad = a/ ( (c**2) * (np.exp(b) - 1.0) )
    return densidad

frecuencia = np.arange(1e+13, 20e+13,1e+13, float) 

densidad100 = planck(frecuencia, 100.)
densidad500 = planck(frecuencia, 500.)
densidad1000 = planck(frecuencia, 1000.)
densidad1500 = planck(frecuencia, 1500.)
densidad2000 = planck(frecuencia, 2000.)

plt.plot(frecuencia*1e15, densidad100, 'r') 
plt.plot(frecuencia*1e15, densidad500, 'g-') 
plt.plot(frecuencia*1e15, densidad1000, 'c-') 
plt.plot(frecuencia*1e15, densidad1500, 'b') 
plt.plot(frecuencia*1e15, densidad2000, 'r-')

plt.ylabel(' Densidad(v)')
plt.xlabel('frecuencia (Hz)')
plt.title('Densidad de energia de un cuerpo negro')
plt.grid(True)
# show the plot
#plt.plot(facecolor=(.18, .31, .31))

plt.show()