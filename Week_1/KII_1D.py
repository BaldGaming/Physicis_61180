import numpy as np
import math
from zcross_simple_example import zero_cross


v0 = float(input("vo: "))
gamma = float(input("gamma: "))
qn = int(input("q#:"))


# 'א: Array
t = np.arange(0, 7, 0.01) # Creates the array
t_size = len(t) # Gets the size


# 'ב: Speed
v = v0 * np.exp(-gamma * t) * np.cos(10 * gamma * t)


# 'ג: Acceleration
dt = 0.01
a = np.gradient(v, dt) # Derivative of v


# 'ד: Place as a form of a function in time
steps = v[:-1] * dt
x = np.concatenate(([0], np.cumsum(steps))) # Integral of v


# 'ה: Place as a form of a function in time
stop_indices = zero_cross(v) # Find all indices where the velocity crosses zero

# Get the time for the 3rd stop (index 2 in the results)
t3rd_stop = t[stop_indices[2]]

Answers = [0, t[:10], v[:10], a[:10], x[:10], t3rd_stop]
print(Answers[qn])
