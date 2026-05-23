import numpy as np
#import matplotlib.pyplot as plt


def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

c=float(input("enter c: "))
qn=int(input("enter qn: "))

b=7e-5
m=2.7/1000
g=9.8
v0=10
alpha=15*np.pi/180

## your code and answers


ANS1=??
ANS2=??

#ouput
Answers=[0,ANS1,ANS2]
print(f'{Answers[qn]:.5g}')
