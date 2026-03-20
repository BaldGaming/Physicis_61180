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
v = np.zeros(t_size) # Initializing an empty array the size of "t".

for i in enumerate(t): # Loop through every index
    v[i] = v0 * math.e^(-gamma * t[i]) * np.cos(10 * gamma * t[i]) # Calculate the speed and put it into "v[i]".
    

# 'ג: Acceleration
a = np.gradient(v) # Derivative of v


# 'ד: Place as a form of a function in time
x = np.cumsum(v) # Integral of v


# 'ה: Place as a form of a function in time
stop_indices = zero_cross(v) # Find all indices where the velocity crosses zero

# Get the time for the 3rd stop (index 2 in the results)
t3rd_stop = t[stop_indices[2]]

Answers = [0, t[:10], v[:10], a[:10], x[:10], t3rd_stop]
print(Answers[qn])
