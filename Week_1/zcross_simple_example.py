# Imports
import numpy as np


def zero_cross(ar_of_a_sampled_f):
    # 1. numpy.sign - returns an array where elements are 1 (pos), -1 (neg), or 0
    signs = np.sign(ar_of_a_sampled_f)

    # 2. numpy.diff - returns an array of differences: [ a[i+1] - a[i], ... ]
    diff = np.diff(signs)

    # 3. numpy.nonzero - returns the indices of all elements that are not zero
    ar_of_sign_change_indxs = np.nonzero(diff)[0]

    return ar_of_sign_change_indxs # We can expect to always get 2 indexes


# Input
v0 = float(input())

# const
g = 9.8  # m/s^2
a = -0.5
b = 1
c = -0.3

t = np.arange(0, 5, 0.01) # Used in the first method.

y = (a * g * t**2) + (b * v0 * t) + (c) # Used in the second method.


# First method:
# We search for sign changes in 'y' (the height)
indices = zero_cross(y)

# We take the difference of the time values at those indices.
time_of_flight = t[indices[1]] - t[indices[0]]

print(f"time of flight: {time_of_flight:.5g} s")

#####################

# Second method:
# We extract the coefficients and calculate the roots.
coefficients = [a * g, b * v0, c]
roots = np.roots(coefficients)

# Then sort them to ensure a consistent positive or negative delta.
sorted_roots = np.sort(roots)
delta = np.diff(sorted_roots)

# We store the result in "time_of_flight".
time_of_flight = delta[0]

print(f"time of flight: {time_of_flight:.5g} s")
