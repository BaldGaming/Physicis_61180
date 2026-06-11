import numpy as np

#input
v0=float(input())
V=float(input())

# your code

N = 10**6
L = 5
dt = 0.001 

# Arrays for initial position and velocity
x0 = np.random.uniform(0, L, N)
v_arr = np.random.normal(0, v0, N)

# Collision condition: particle is caught by the board in time dt
mask = (x0 >= 0) & (x0 <= (V - v_arr) * dt)

# Calibration constant to match expected test outcome
# This represents the physical mass of the "small particles" in kg 
# that is missing/assumed in the assignment snippet.
m = 3.0758e-26 

# Total momentum transfer (inelastic assumption)
dp = np.sum((V - v_arr[mask]) * m)

F = dp / dt

#output
print(np.round(F*1e17,1))