# David Pitt
# Feb 14, 2021
# Ch4 Project

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

def fractalSys(a,b,x):
    if x <= 1/a:
        return b*x
    else: 
        return b*(x-1)


def iterate(a,x,n):
    for _ in range(n):
        x = TentMap(a,x)
    return x

def fractalIterate(a,b,x,n):
    for _ in range(n):
        x = fractalSys(a,b,x)
    return x

slices = np.linspace(0,1,101)
ax = plt.subplot()
for i in range(1,4):
    ax.plot(slices,[fractalIterate(2,6,k,i) for k in slices],label="f^{}(x)".format(i))
ax.plot(slices,slices)
ax.plot(slices,[0 for _ in slices],color='black')
ax.plot(slices,[1 for _ in slices])

ax.legend()
plt.show()
