import numpy as np

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

#input
m=float(input())

#your code

# This function simulates the non-linear spring motion
def simulate_nonlinear(x0, v0, m, kappa, dt, t_last):
    t = np.arange(0, t_last, dt)
    n_steps = len(t)
    x = np.zeros(n_steps)
    v = np.zeros(n_steps)
    
    x[0] = x0
    v[0] = v0
    
    for i in range(n_steps - 1):
        v[i+1] = v[i] - (kappa / m) * (x[i]**3) * dt
        x[i+1] = x[i] + v[i+1] * dt
        
    return t, x, v

kappa = 5.0
dt = 1e-3
t_last = 10.0
x0_list = [1.0, 1.4, 1.8, 2.2]
A_list = []
f_list = []

for x0 in x0_list:
    t, x, v = simulate_nonlinear(x0, 0.0, m, kappa, dt, t_last)
    
    A = (np.max(x) - np.min(x)) / 2.0
    A_list.append(A)
    
    zc = zero_cross(x)
    T = 2 * (t[zc[-1]] - t[zc[0]]) / (len(zc) - 1)
    f_list.append(1.0 / T)

fit = np.polyfit(A_list, f_list, 1)
slope = fit[0]

#ouput
print(f'{slope:.4g}')