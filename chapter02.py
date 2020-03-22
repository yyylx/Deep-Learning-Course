import numpy as np
import math

X=np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
Y=np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
X1 = np.mean(X)
Y1 = np.mean(Y)
w1=0
w2=0
i=0
for i in range(X.size):
    w1+=((X[i]-X1) * (Y[i]-Y1))
    w2+=math.pow(X[i]-X1,2)
w=w1/w2
print("w的值为:",w)
print("b的值为:",Y1-w*X1)