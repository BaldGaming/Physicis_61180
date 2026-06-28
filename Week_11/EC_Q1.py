# Electric Circuits Q1 - solve linear equations representing an electrical circuit
import numpy as np

# input
V1=float(input())

#your code - assign the requested current to a variable named I

# Matrix A representing the coefficients of [I, I1, I2, I3]
# Eq 1 (Node): I - I1 - I2 - I3 = 0
# Eq 2 (Loop 1 - Main and Branch 1): 11*I + 2*I1 = V1 - 1
# Eq 3 (Loop 2 - Branch 1 and 2): 2*I1 - 2*I2 = -1
# Eq 4 (Loop 3 - Branch 2 and 3): 2*I2 - 8*I3 = 3
A = np.array([
    [ 1, -1, -1, -1],
    [11,  2,  0,  0],
    [ 0,  2, -2,  0],
    [ 0,  0,  2, -8]
])

b = np.array([0, V1 - 1, -1, 3])

# Solve the system of linear equations
x = np.linalg.solve(A, b)

# I is the first element in our variable vector x
I = x[0]

#output
print(f'Current drawn from main source: {I:1.4} A')