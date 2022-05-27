import numpy as np 
import matplotlib.pyplot as plt

f = 60   #frequencia
T = 1/f
A = 220*np.sqrt(2) #amplitude
t = np.arange(0,2*T,T/200)
y = A * np.sin(2*np.pi*f*t)

plt.title("Demonstração Matplotlib")
plt.xlabel("Tempo [s]")
plt.ylabel("Tensão [V]")
plt.grid('Minor')
plt.plot(t,y)
plt.show()


