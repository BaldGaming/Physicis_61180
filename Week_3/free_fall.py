import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    # returns an array of indices where ar changes sign
    H1t = np.sign(ar)
    H1s = np.abs(H1t[:-1] - H1t[1:])
    return np.nonzero(H1s)[0]

# inputs
V0x = float(input('enter V_ox: '))
V0y = float(input('enter V_oy: '))
qn = int(input('enter qn: '))
print()

# your code

# const
g = 9.8 

# Create a time array in the specified range.
t_max = (2.5 * V0y) / g
t, dt = np.linspace(0, t_max, 3000, endpoint=False, retstep=True)

# We create the acceleration arrays using the required numpy commands.
ax = np.zeros_like(t)
ay = -g * np.ones_like(t)

# Numerical integration for velocity components.
vx = np.zeros_like(t)
vx[0] = V0x
vx[1:] = V0x + np.cumsum(ax[:-1]) * dt

vy = np.zeros_like(t)
vy[0] = V0y
vy[1:] = V0y + np.cumsum(ay[:-1]) * dt

# Numerical integration for position components.
x = np.zeros_like(t)
x[0] = 0.0
x[1:] = 0.0 + np.cumsum(vx[:-1]) * dt

y = np.zeros_like(t)
y[0] = 0.0
y[1:] = 0.0 + np.cumsum(vy[:-1]) * dt

# We search for sign changes in 'y' (the height).
indices = zero_cross(y)

# We take the last index to safely capture the landing.
land_idx = indices[-1]

# 1.
Ans1 = t[land_idx] 

# 2.
Ans2 = x[land_idx] 

# 3.
Ans3 = (2 * V0y) / g 

# 4.
Ans4 = V0x * Ans3 

Answers = [0, Ans1, Ans2, Ans3, Ans4]

# output
print(f'{Answers[qn]:.5g}')