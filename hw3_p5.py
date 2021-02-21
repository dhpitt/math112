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
    if x <= 1/2:
        return -b*(x-1/2)**6
    else: 
        return -b*((x-1/2)**6)

def testFive(x):
    if x <= 2/5:
        return 5*x
    elif x <= 1/2:
        return 6-10*x
    elif x < 3/5: 
        return -4+10*x
    else:
        return 5*(1-x)

def iterate(a,x,n):
    for _ in range(n):
        x = TentMap(a,x)
    return x

def fractalIterate(a,b,x,n):
    for _ in range(n):
        x = fractalSys(a,b,x)
    return x

def testFiveIter(x,n):
    for _ in range(n):
        x = testFive(x)
    return x

slices = np.linspace(0,1,101)
ax = plt.subplot()
for i in range(1,7):
    ax.plot(slices,[fractalIterate(3,7,k,i) for k in slices],label="f^{}(x)".format(i))
    #ax.plot(slices,[fra(k,i) for k in slices],label="f^{}(x)".format(i))
#ax.plot(slices,slices)
ax.plot(slices,[0 for _ in slices],color='black')
#ax.plot(slices,[1 for _ in slices])
ax.set(xlim=[0,1],ylim=[-5,5])

ax.set(xlabel="x")
ax.set(ylabel="f^n(x)")
ax.set(title='Graph of the first 3 iterates of ' + r'$f_{3,7}(x)$')

ax.legend()
plt.show()
