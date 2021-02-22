# David Pitt
# Feb 15
# Module 5


import numpy as np
import math
from cobwebGenerator import AnnotatedFunction, plot_cobweb
import matplotlib.pylab as plt
from scipy.optimize import fsolve

def h(c,x):
    if x <= 1/4:
        return c*x
    else:
        return c/3*(1-x)

def iterator(c,x,n):
    for _ in range(n):
        x = h(c,x)
    return x

#plt.style.use("seaborn-pastel")
slices = np.linspace(0,1,10001)
ax = plt.subplot()

#for i in range(8,17):
    #ax.plot(slices,[iterator(i/4,k,30) for k in slices],label='c = {}'.format(str(i/4)))


    #ax.plot(slices,[fra(k,i) for k in slices],label="f^{}(x)".format(i))
ax.plot(slices,slices)
ax.plot(slices,[0 for _ in slices],color='black')
ax.plot(slices,[1 for _ in slices])
#ax.plot(slices,[iterator(4,i,2) for i in slices], label=r'$h^2(x)$')
#ax.plot(slices,[iterator(4,i,3) for i in slices], label=r'$h^3(x)$')
#ax.plot(slices,[iterator(4,i,3) for i in slices], label=r'$h^4(x)$')
ax.plot(slices,[h(3,i) for i in slices], label=r'$h^4(x)$')


ax.set(xlim=[0,1],ylim=[0,1.5])

ax.set(xlabel="x")
ax.set(ylabel=r'$h(x)$')
ax.set(title='h(x) IC separation')

ax.legend()
plt.show()