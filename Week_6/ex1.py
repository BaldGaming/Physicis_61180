import numpy as np

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    b=np.sign(ar)
    d=np.diff(b)
    return np.nonzero(d)[0]



# inputs
m=float(input("m:"))
qn=int(input("qn:"))

##
#your code



##
# output
if qn==1:
    print(np.round(V1,3))
elif qn==2:
    print(np.round(W2,3))
elif qn==3:
    print(np.round(theta_break,3))
