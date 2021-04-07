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

#G3.5
'''
ax.plot(slices,slices)
ax.plot(slices,[0 for _ in slices],color='black')
ax.plot(slices,[1 for _ in slices])
for j in range(5):  
    ax.plot(slices,[g(3.5,i,j) for i in slices], label=r'$g^{}(x)$'.format(j))



ax.set(xlim=[0,1],ylim=[0,1.5])

ax.set(xlabel="x")
ax.set(ylabel=r'$g^n(x)$')
ax.set(title='Periodic Point Finder, g3.5')

ax.legend()
plt.show()
'''
plt.style.use('seaborn-pastel')

# G4
ax.plot(slices,slices,label=r'y=x')
ax.plot(slices,[0 for _ in slices],color='black')
ax.plot(slices,[1 for _ in slices])
for j in range(1,7):  
    ax.plot(slices,[g(4,i,j) for i in slices], label=r'$g^{}(x)$'.format(j))



ax.set(xlim=[0,1],ylim=[0,1.5])

ax.set(xlabel="x")
ax.set(ylabel=r'$g^n(x)$')
ax.set(title='Periodic Point Finder, g4')

ax.legend()
plt.show()