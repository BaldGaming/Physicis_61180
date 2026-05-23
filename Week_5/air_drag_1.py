#imports and def
import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    sign_ar=np.sign(ar)
    sign_change_ar=np.abs(sign_ar[:-1]-sign_ar[1:])
    return np.nonzero(sign_change_ar)[0]

#input
sn=int(input())
v0=float(input())
m=float(input())
b=float(input())

#your code

#output
if sn==1:
    print(t1)
if sn==2:
    print(t2)