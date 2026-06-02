import numpy as np
import matplotlib.pyplot as plt

# variables
m = 0.1
g = 9.8
b = 0.2
c = 0.3
h = 0.5
v0 = 10
alpha = 30 * (np.pi / 180)
dt = 0.001

# starting conditions
x = 0
y = h
vx = v0 * np.cos(alpha)
vy = v0 * np.sin(alpha)
t = 0

# empty lists to then put data from each iteration in
xList = [x]
yList = [y]
vyList = [vy]
tList = [t]

# "euler calculation".. runs until the ball hits the floor
while y >= 0:
    # current speed
    v = np.sqrt(vx**2 + vy**2)

    # acceleration
    ax = -(1 / m) * (b + c * v) * vx
    ay = -g - (1 / m) * (b + c * v) * vy

    # update next speed
    vx = vx + ax * dt
    vy = vy + ay * dt

    # update next position
    x = x + vx * dt
    y = y + vy * dt

    # update time
    t = t + dt

    # update the lists
    xList.append(x)
    yList.append(y)
    vyList.append(vy)
    tList.append(t)

# update the "end stats"
maxHeightTime = tList[yList.index(max(yList))]

returnHeightTime = 0
for i in range(len(yList)):
    if yList[i] <= h and yList[i] <= h:
        returnHeightTime = tList[i]
        break

totalTime = tList[-1]
horizontalRange = xList[-1]

# parabola fit
# calculates the A, B, and C coefficients for the bestfit parabola
coefficients = np.polyfit(xList, yList, 2)
# plugs the x values into the new parabola equation to generate a list of y values without air resistance
yPara = np.polyval(coefficients, xList)

# RMS calculation
# converts the list of simulated y values into a NumPy array, and parabola y values
yArr = np.array(yList)
yParaArr = np.array(yPara)
# calculates the RMS
rms = np.sqrt(np.mean((yArr - yParaArr) ** 2)) / (np.max(yArr) - np.min(yArr))

# display the stats
print(f"Time to max height: {maxHeightTime:.3f} s")
print(f"Time to return to starting height: {returnHeightTime:.3f} s")
print(f"Total flight time: {totalTime:.3f} s")
print(f"Range: {horizontalRange:.3f} m")
print(f"RMS: {rms:.5f}")

# graph
plt.plot(xList, yList, label="Euler calculation", color="red")
plt.plot(xList, yPara, label="Parabola", color="blue", linestyle="--")
plt.legend()
plt.show()