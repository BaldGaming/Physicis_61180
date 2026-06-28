#imports and def
import numpy as np

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    sign_ar=np.sign(ar)
    sign_change_ar=np.abs(sign_ar[:-1]-sign_ar[1:])
    return np.nonzero(sign_change_ar)[0]

#input
sn=int(input())
v0=float(input())
m=float(input())
b=float(input())

#your code

# consts
g = 9.8
dt = 1e-3

t = np.arange(0, 3, dt)
v = np.zeros_like(t)
y = np.zeros_like(t)

v[0] = v0
y[0] = 0

# Euler integration
for i in range(len(t)-1):
    a = -g - (b / m) * v[i]
    v[i+1] = v[i] + a * dt
    y[i+1] = y[i] + v[i] * dt

# Max height time (where velocity crosses zero)
v_cross = zero_cross(v)
t1 = t[v_cross[0]]

# Total flight time (where height crosses zero again)
y_cross = zero_cross(y)
t_total = t[y_cross[-1]]

# The time of the return trip ONLY (Total time minus ascent time)
t2 = t_total - t1

#output
if sn==1:
    print(np.round(t1, 3))
if sn==2:
    print(np.round(t2, 3))