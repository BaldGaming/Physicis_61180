import numpy as np
import matplotlib.pyplot as plt

# Input
A=float(input("A:"))
B=float(input("B:"))
qn=int(input("qn:"))

# 1.
if A > B:
    C = A - B
else:
    C = B - A

# 2.
D = A + B

# 3.
dx = 0.01
x = np.arange(0,10,dx)
print(x)

func = np.sin(x+2)*np.cos(2*x-3)
print(func)

plt.plot(x,func)
plt.show()

max_no = 5


#output
if qn==1: 
    print(f'{C:.5g}')
elif qn==2: 
    print(f'{D:.5g}')
elif qn==3:
    print(max_no)