import numpy as np

def to_array(s):
    return np.fromstring(s.strip("[]"), sep=" ")

#input
q1=float(input())
q2=float(input())
q3=float(input())
r1=to_array(input())
r2=to_array(input())
r3=to_array(input())
qn=int(input())

k=9e9
# your code

# Part 1: Finding Q based on Tzipi's hypothesis (F proportional to 1/r^2)
r_vals = np.array([1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8])
F_vals = np.array([4.32, 2.97, 2.18, 1.71, 1.34, 1.08, 0.91, 0.77, 0.64, 0.55])

# Fit linear polynomial to F vs (1/r^2) to find the slope
fit = np.polyfit(1.0 / (r_vals**2), F_vals, 1)
slope = fit[0]
Q_part_1 = np.sqrt(slope / k)

# Part 2: Vector force calculation on q3
r13 = r3 - r1
r23 = r3 - r2

mag_r13 = np.linalg.norm(r13)
mag_r23 = np.linalg.norm(r23)

F13 = k * q1 * q3 * r13 / (mag_r13**3)
F23 = k * q2 * q3 * r23 / (mag_r23**3)

F_total = F13 + F23

F3x = F_total[0]
F3y = F_total[1]
F3z = F_total[2]


# output
if qn==1: print(f'{Q_part_1:.2g}')
if qn==2: print(f'{F3x:.5g},{F3y:.5g},{F3z:.5g}')