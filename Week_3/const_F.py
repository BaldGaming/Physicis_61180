import numpy as np

# Input
F = float(input())
v0 = float(input())
L = float(input())
qn = int(input())

# const
m = 1

# 1.
D_stop = (v0 ** 2) / (2 * F)

if L <= D_stop:
    t_1 = (v0 - np.sqrt(v0 ** 2 - 2 * F * L)) / F
else:
    t_1 = (v0 / F) + np.sqrt(2 * F * L - v0 ** 2) / F

# 2.
dt = 0.01
t_2 = 0.0
v_curr = v0
D_curr = 0.0

while D_curr < L:
    v_curr -= F * dt
    D_curr += np.abs(v_curr) * dt
    t_2 += dt

# 3.
dt_3 = 0.01
t_3 = 0.0
D_3 = 0.0

while D_3 < L:
    vx = v0 + t_3 ** 2
    vy = 400 * (t_3 ** 3)
    v_mag = np.sqrt(vx ** 2 + vy ** 2)
    D_3 += v_mag * dt_3
    t_3 += dt_3

# output
Answers = [0, t_1, t_2, t_3]
ans = Answers[qn]
print(f'{ans:.3g}')