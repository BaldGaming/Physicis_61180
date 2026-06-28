import numpy as np
#import matplotlib.pyplot as plt

#input
v0x=float(input())
v0y=float(input()) # test using v0x=0 v0y=4.5e6 m/s #
x0= float(input()) # x0=1.5e-11 m    y0=0
y0= float(input())
qn= int(input())

# your code
k = 9e9
e = 1.6e-19
m_e = 9.1e-31

dt = 1e-20
t_last = 1.2e-16
n_steps = int(t_last / dt) + 1

x = np.zeros(n_steps)
y = np.zeros(n_steps)
vx = np.zeros(n_steps)
vy = np.zeros(n_steps)

x[0] = x0
y[0] = y0
vx[0] = v0x
vy[0] = v0y

for i in range(n_steps - 1):
    r_sq = x[i]**2 + y[i]**2
    r3 = r_sq**1.5
    
    ax = - (k * e**2 * x[i]) / (m_e * r3)
    ay = - (k * e**2 * y[i]) / (m_e * r3)
    
    vx[i+1] = vx[i] + ax * dt
    vy[i+1] = vy[i] + ay * dt
    x[i+1] = x[i] + vx[i+1] * dt
    y[i+1] = y[i] + vy[i+1] * dt

r = np.sqrt(x**2 + y**2)
r_max = np.max(r)
r_min = np.min(r)

part1 = 'c'
part2 = 'd'
part3 = (r_max - r_min) / (r_max + r_min)


# output
if qn==1:
    print(f'{part1}')
if qn==2:
    print(f'{part2}')   
if qn==3:
    print(f'{part3:.3g}')