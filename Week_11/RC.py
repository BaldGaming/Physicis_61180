import numpy as np

C=float(input())
R=float(input())
w0=float(input())
V0=float(input())

#your code
n_steps = 1000
dt = 20 * R * C / 1000
t = np.arange(n_steps) * dt

q = np.zeros(n_steps)
I = np.zeros(n_steps)

for i in range(n_steps - 1):
    I[i] = (V0 * np.sin(w0 * t[i]) - q[i] / C) / R
    q[i+1] = q[i] + I[i] * dt

Imax = np.max(I[500:])

print(f'{Imax:.5g}')