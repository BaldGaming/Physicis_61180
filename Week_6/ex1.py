import numpy as np

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    b=np.sign(ar)
    d=np.diff(b)
    return np.nonzero(d)[0]

# inputs
m=float(input("m:"))
qn=int(input("qn:"))

##
#your code

# consts
g = 9.8
R = 1.0
dtheta = 1e-3

# Create the angle array from 0 to pi/2
theta = np.arange(0, np.pi/2, dtheta)

# Initialize state arrays
W = np.zeros_like(theta)
K = np.zeros_like(theta)
v = np.zeros_like(theta)
N_force = np.zeros_like(theta)

# Initial conditions (starts from rest at highest point)
v[0] = 0
K[0] = 0
W[0] = 0
N_force[0] = m * g * np.sin(theta[0]) + (m * v[0]**2) / R

# Numerical integration using the work-energy theorem
for i in range(len(theta)-1):
    # Work done by gravity in this small step
    dW = m * g * np.cos(theta[i]) * R * dtheta
    
    W[i+1] = W[i] + dW
    K[i+1] = W[i+1] 
    v[i+1] = np.sqrt(2 * K[i+1] / m)
    
    # Normal force at the new position
    N_force[i+1] = m * g * np.sin(theta[i+1]) + (m * v[i+1]**2) / R


# 1. & 2. Velocity and Work at the bottom of the track
V1 = v[-1]
W2 = W[-1]

# 3. Angle where Normal force exceeds 45 N
crossings = zero_cross(N_force - 45)

if len(crossings) > 0:
    theta_break = theta[crossings[0]]
else:
    theta_break = 999

##
# output
if qn==1:
    print(np.round(V1,3))
elif qn==2:
    print(np.round(W2,3))
elif qn==3:
    print(np.round(theta_break,3))