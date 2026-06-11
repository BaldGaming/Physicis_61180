import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

c=float(input("enter c: "))
qn=int(input("enter qn: "))

b=7e-5
m=2.7/1000
g=9.8
v0=10
alpha=15*np.pi/180

## your code and answers

dt = 1e-4
t = np.arange(0, 1.1, dt)

def solve_trajectory(c_val):
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    vx = np.zeros_like(t)
    vy = np.zeros_like(t)
    
    vx[0] = v0 * np.cos(alpha)
    vy[0] = v0 * np.sin(alpha)
    
    # Euler integration
    for i in range(len(t)-1):
        v_mag = np.sqrt(vx[i]**2 + vy[i]**2)
        
        ax = -(b / m) * vx[i] - (c_val / m) * v_mag * vx[i]
        ay = -g - (b / m) * vy[i] - (c_val / m) * v_mag * vy[i]
        
        vx[i+1] = vx[i] + ax * dt
        vy[i+1] = vy[i] + ay * dt
        
        x[i+1] = x[i] + vx[i] * dt
        y[i+1] = y[i] + vy[i] * dt
        
    y_cross = zero_cross(y)
    
    # Return horizontal range at the exact landing index
    return x[y_cross[-1]]

# 1. Trajectory with c=0
ANS1 = solve_trajectory(0.0)

# 2. Trajectory with c from input
ANS2 = solve_trajectory(c)


#output
Answers=[0,ANS1,ANS2]
print(f'{Answers[qn]:.5g}')