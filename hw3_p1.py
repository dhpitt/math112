# David Pitt
# Feb 8 2020
# HW3
# Pr1

import numpy as np
import math
from cobwebGenerator import AnnotatedFunction, plot_cobweb
import matplotlib.pylab as plt
from scipy.optimize import fsolve

def TentMap(a,x):
    if x <= 1/2:
        return a*x
    else: 
        return a - a*x

def iterate(a,x,n):
    for _ in range(n):
        x = TentMap(a,x)
    return x

slices = np.linspace(0,1,101)
ax = plt.subplot()
for i in range(1,4):
    ax.plot(slices,[iterate(4,k,i) for k in slices],label="f^{}(x)".format(i))
ax.plot(slices,slices)
ax.plot(slices,[0 for _ in slices],color='black')
ax.plot(slices,[1 for _ in slices])

ax.legend()
plt.show()

def orbit(a,x0,n):
    o = []
    for _ in range(n):
        o.append(x0)
        x0 = TentMap(a,x0)
    return o

print(orbit(3,.25,10))

def period3Root(x):
    return iterate(3,x,3) - x

ans = set()
for i in slices:
    ans.add(fsolve(period3Root,i)[0])

#print(ans)