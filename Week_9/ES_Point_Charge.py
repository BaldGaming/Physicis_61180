import numpy as np

#inputs
x0=float(input())
y0=float(input())
qn=int(input())

#your code
k = 9e9
q = 1.0 / 9.0 * 1e-9
kq = k * q  # This simplifies perfectly to 1.0

# Part 1: Analytical
r0 = np.sqrt(x0**2 + y0**2)
Exx0y0_1 = kq * x0 / r0**3
Eyx0y0_1 = kq * y0 / r0**3

# Part 2: Grid Direct Calculation
x_grid2 = np.linspace(-4, 4, 81)
y_grid2 = np.linspace(-4, 4, 81)
X2, Y2 = np.meshgrid(x_grid2, y_grid2)
R2 = np.sqrt(X2**2 + Y2**2)

with np.errstate(divide='ignore', invalid='ignore'):
    Ex2 = kq * X2 / R2**3
    Ey2 = kq * Y2 / R2**3

ix2 = np.argmin(np.abs(x_grid2 - x0))
iy2 = np.argmin(np.abs(y_grid2 - y0))
Exx0y0_2 = Ex2[iy2, ix2]
Eyx0y0_2 = Ey2[iy2, ix2]

# Part 3: Potential Gradient Calculation
x_grid3 = np.linspace(-4, 4, 801)
y_grid3 = np.linspace(-4, 4, 801)
X3, Y3 = np.meshgrid(x_grid3, y_grid3)
R3 = np.sqrt(X3**2 + Y3**2)

with np.errstate(divide='ignore', invalid='ignore'):
    phi3 = kq / R3

grad_y, grad_x = np.gradient(phi3, 0.01, 0.01)
Ex3 = -grad_x
Ey3 = -grad_y

ix3 = np.argmin(np.abs(x_grid3 - x0))
iy3 = np.argmin(np.abs(y_grid3 - y0))
Exx0y0_3 = Ex3[iy3, ix3]
Eyx0y0_3 = Ey3[iy3, ix3]

#ouput
if qn==1:
    print(f"Output={Exx0y0_1:.5g}\n{Eyx0y0_1:.5g}")
if qn==2:
    print(f"Output={Exx0y0_2:.5g}\n{Eyx0y0_2:.5g}")
if qn==3:
    print(f"Output={Exx0y0_3:.5g}\n{Eyx0y0_3:.5g}")