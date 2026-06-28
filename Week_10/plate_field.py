import numpy as np

L=float(input())

# your code
dx = 0.001 * L
x0 = np.arange(-L, L, dx)
z = 0.01 * L

# dE = (2 * k * sigma * dx / (x0^2 + z^2)) * (-x0*x_hat + z*z_hat)
# Factoring out k * sigma gives us our equations for a1 and a2
a1 = np.sum((2 * dx * (-x0)) / (x0**2 + z**2))
a2 = np.sum((2 * dx * z) / (x0**2 + z**2))


# output
print(f'Output={a1:.3f},{a2:.3f}')