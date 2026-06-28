import numpy as np

x0=float(input("initial position: "))
v0=float(input("initial velocity: "))

# This function calculates Simple Harmonic Motion using Algorithm A1 (Standard Euler)
def Simple_HM_A1(x0,v0,dt,t_last):
    n_steps = int(t_last / dt) + 1
    t = np.linspace(0, t_last, n_steps)
    x = np.zeros(n_steps)
    v = np.zeros(n_steps)
    
    x[0] = x0
    v[0] = v0
    w0_sq = 40.0 / 2.0 # k/m
    
    for i in range(n_steps - 1):
        v[i+1] = v[i] - w0_sq * x[i] * dt
        x[i+1] = x[i] + v[i] * dt
        
    return t, x, v
    
# This function calculates Simple Harmonic Motion using Algorithm A2 (Euler-Cromer)
def Simple_HM_A2(x0,v0,dt,t_last):
    n_steps = int(t_last / dt) + 1
    t = np.linspace(0, t_last, n_steps)
    x = np.zeros(n_steps)
    v = np.zeros(n_steps)
    
    x[0] = x0
    v[0] = v0
    w0_sq = 40.0 / 2.0 # k/m
    
    for i in range(n_steps - 1):
        v[i+1] = v[i] - w0_sq * x[i] * dt
        x[i+1] = x[i] + v[i+1] * dt
        
    return t, x, v
    
    
dt=0.01
t_last=10
t,x_A1,v_A1=Simple_HM_A1(x0,v0,dt,t_last)
t,x_A2,v_A2=Simple_HM_A2(x0,v0,dt,t_last)

w0 = np.sqrt(40.0 / 2.0)
x_th = x0 * np.cos(w0 * t) + (v0 / w0) * np.sin(w0 * t)

D1=np.abs(x_th[300]-x_A1[300])
D2=np.abs(x_th[300]-x_A2[300])

#output
print(f'{x_A1[300]:.5g}')
print(f'{x_A2[300]:.5g}')
print(f'{D1:.5g}')
print(f'{D2:.5g}')