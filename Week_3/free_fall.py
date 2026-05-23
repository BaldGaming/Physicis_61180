import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]
#inputs
V0x=float(input('enter V_ox: '))
V0y=float(input('enter V_oy: '))
qn=int(input('enter qn: '))
print()

#your code


Ans1=??
Ans2=??
Ans3=??
Ans4=??

Answers=[0,Ans1,Ans2,Ans3,Ans4]
#output
print(f'{Answers[qn]:.5g}')