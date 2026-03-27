import numpy as np
import matplotlib.pyplot as plt


def zero_cross(ar):
    # returns an array of indices where ar changes sign
    H1t = np.sign(ar)
    H1s = np.abs(H1t[:-1] - H1t[1:])
    return np.nonzero(H1s)[0]

# input
T1 = float(input("enter T_one: "))
T2 = float(input("enter T_two: "))
R = 40
qn = int(input("enter question no.: "))

# your code
t = T1 / 6

# Car 1 & 2 calculations
θ1, θ2 = (2 * np.pi / T1) * t, (2 * np.pi / T2) * t
X1, Y1 = R * np.cos(θ1), R * np.sin(θ1)
X2, Y2 = R * np.cos(θ2), R * np.sin(θ2)

# output
if qn == 1:
    print(f"{X1:.5g},{Y1:.5g} m")

    # Draws the Track
    angles = np.linspace(0, 2 * np.pi, 100)
    plt.plot(R * np.cos(angles), R * np.sin(angles), "b-")

    # Draws the Cars
    plt.plot(X1, Y1, "ro", label = "Car 1")  # Red circle
    plt.plot(X2, Y2, "go", label = "Car 2")  # Green circle

    # Draws the Center
    plt.plot(0, 0, "y.")

    plt.axis("equal")
    plt.legend()
    plt.show()
    
if qn == 2:
    d = np.sqrt((X2 - X1)**2 + (Y2 - Y1)**2) # Chord length formula
    print(f"{d:.5g} m")
    
if qn == 3:
    s = R * (θ1 - θ2) # Arc length formula
    print(f"{s:.5g} m")

if qn == 4:
    time_arr = np.linspace(0, 10*T2, 10000) # Creates the time array

    # Coordinates as arrays for all time points
    θ1_arr, θ2_arr = (2 * np.pi / T1) * time_arr, (2 * np.pi / T2) * time_arr
    X1_arr, Y1_arr = R * np.cos(θ1_arr), R * np.sin(θ1_arr)
    X2_arr, Y2_arr = R * np.cos(θ2_arr), R * np.sin(θ2_arr)

    D = np.sqrt((X2_arr - X1_arr)**2 + (Y2_arr - Y1_arr)**2) # Distance
    
    dD = np.gradient(D) # Find the rate of change of the distance
    indices = zero_cross(dD) # Find all points where the distance stops decreasing/increasing

    plt.figure(figsize=(10, 6))
    plt.plot(time_arr, D, 'y-', label="Distance between cars")
    plt.axhline(0, color='black', lw=1, alpha=0.3) # Ground line for reference
    plt.xlabel("Time (s)")
    plt.ylabel("Distance (m)")
    plt.title(f"Numerical Search for T3 (T1={T1}, T2={T2})")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.show()

    T3_numeric = time_arr[indices[1]]
    print(f"{T3_numeric:.5g}")

if qn == 5:
    T3_analytic = (T1 * T2) / (T2 - T1)
    print(f"{T3_analytic:.5g}")
