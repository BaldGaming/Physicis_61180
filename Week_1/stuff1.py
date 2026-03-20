import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,2000)

a = 3
b = 2
c = 2
alpha = 0.7
omega = 1.5

x = a*t
y = b*np.sin(omega*t)
z = c*np.exp(-alpha*t)

plt.plot(t,x)
plt.plot(x,z)
plt.plot(y,x)