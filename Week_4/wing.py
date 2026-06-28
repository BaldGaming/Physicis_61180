import numpy as np

def zero_cross(ar):
    # returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

# input
V=float(input('enter V: '))
alp=float(input('enter alpha: '))
qn=int(input('enter question no.: '))
print()

# consts
rho=1.3 # kg/m^3 (air density)
A=18 # m^2 (wing area)

# your code

# 1. & 2.
alp_rad = np.radians(alp)

Fy = 2 * rho * A * (V**2) * (np.sin(alp_rad)**2) * np.cos(alp_rad)
Fx = 2 * rho * A * (V**2) * (np.sin(alp_rad)**3) 

# 3.
# Fy = 10 * Fx -> cos(alpha) = 10 * sin(alpha) -> tan(alpha) = 0.1
# Storing alpha in degrees and applying the requested 0.01 precision.
alpha = np.degrees(np.arctan(0.1))
alpha = round(alpha, 2)

# 4.
# Fy_new = 1000 * 10 = 10000 N
# We use the alpha we just found (converted back to radians for calculation).
alpha_rad = np.radians(alpha)
V4 = np.sqrt(10000 / (2 * rho * A * (np.sin(alpha_rad)**2) * np.cos(alpha_rad)))


Answers=[0,Fy,Fx,alpha,V4]
print(f'{Answers[qn]:.5g}')