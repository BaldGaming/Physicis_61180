import numpy as np
import matplotlib.pyplot as plt

qn = int(input("enter question number: "))
a = float(input("enter acceleration: "))
print()

if qn == 2:
    t = float(input("enter t: "))
    ## your answer
    v = a * t # Velocity

    ## output
    print(f"v={v:.5g} m/s")

if qn == 3:
    t = float(input("enter t: "))
    ## your answer
    x = 0.5 * a * t^2 # Position

    ## output
    print(f"x={x:.5g} m")

if qn == 4:
    v = float(input("enter v: "))
    ## your answer
    x = (v^2) / (2*a) # Position from velocity

    ## output
    print(f"x={x:.5g} m")

if qn == 7:
    ANS = TRUE
    print(ANS)
