
import numpy as np

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]


#input
V=float(input('enter V: '))
alp=float(input('enter alpha: '))
qn=int(input('enter question no.: '))
print()

# consts
rho=1.3 # kg/m^3 (air density)
A=18 # m^2 (wing area)

# your code

Fy=??
Fx=?? 
alpha=??
V4=??



Answers=[0,Fy,Fx,alpha*180/np.pi,V4]
print(f'{Answers[qn]:.5g}')
