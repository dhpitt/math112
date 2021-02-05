import matplotlib.pylab as plt
import math
import numpy as np
from scipy.optimize import fsolve

def doubling_Map(x):
    if x > 0.5:
        return 2*x-1
    else:
        return 2*x

def dN(x,n=5):
    for _ in range(n):
        x = doubling_Map(x)
    return x

def dNRoots(x):
    return(dN(x)-x)
X = list(range(101))
X = np.divide(X,100)

def tripling_Map(x):
    return 3*x%1

def a_map(x,a):
    return a*x%1

slices = list(range(501))
slices = np.divide(slices,500)

period5 = set()

for i in X:
    period5.add(round(fsolve(dNRoots,i)[0],4))

print(period5)
print(len(period5))

ax = plt.subplot()
ax.plot(slices,slices)
ax.plot(slices,[a_map(i,12) for i in slices])
#ax.plot(slices,[tripling_Map(i) for i in slices])
#ax.plot(slices,[dN(i) for i in slices])
#ax.scatter(list(period5),list(period5))
plt.show()
