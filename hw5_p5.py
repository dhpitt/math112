# David Pitt
# Feb 22
# Module 6 Exploration - In-class Activity

import numpy as np
import math
from cobwebGenerator import AnnotatedFunction, plot_cobweb
import matplotlib.pylab as plt
from scipy.optimize import fsolve

def g1(c,x):
    return c*x*(1-x)


def g(c,x,n):
    for _ in range(n):
        x = g1(c,x)
    return x

slices = np.linspace(0,1,10001)
ax = plt.subplot()

three_cycle = [0.117,0.413,0.970]
ax.plot(slices,slices,label='y=x')
ax.plot(slices,[g(4,i,1) for i in slices])
ax.scatter(three_cycle,[g(4,i,1) for i in three_cycle],color='red')


ax.set(xlim=[0,1],ylim=[0,1.5])

ax.set(xlabel="x")
ax.set(ylabel=r'$g_4(x)$')
#ax.set(title='')

for i in slices:
    if round(g(4,i,1),3) == 0.970:
        print(i)

def subintervalMap(a,b):
    bound1 = set()
    bound2 = set()
    for i in slices:
        f_i = round(g(4,i,1),3)
        if f_i == a and i > 0.117 and i < 0.413:
            bound1.add(round(i,3))
        elif f_i == b and i > 0.117 and i < 0.413:
            bound2.add(round(i,3))
    return(bound1,bound2)

print(subintervalMap(0.671,0.821))
ax.legend()
# plt.show()