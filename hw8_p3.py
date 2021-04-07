import matplotlib.pylab as plt
from matplotlib.pyplot import plot
import numpy as np
import math
from numpy.lib.polynomial import polyint
from scipy.optimize import fsolve

def fd(z):
    return(np.exp(math.pi**2*1j)*z)

    
x0 = [1+1j,2-3*1j,-1+2*1j,-1-3*1j,2,-1*1j,2*1j]
ax = plt.subplot()

ltbs = []
for x in x0:
    behavior = [x]
    for _ in range(6):
        x = fd(x)
        behavior.append(x)
    ltbs.append(behavior)




for i in ltbs:
    ax.plot([x.real for x in i],[x.imag for x in i])
    print(i)


#ax.plot([x.real for x in ltbs[0]],[x.imag for x in ltbs[0]])

#ax.set(xlim=[0,1],ylim=[0,1])
ax.set(xlabel='Re(z)',ylabel='Im(z)')
ax.set_title("End behavior of f2")



plt.show()
