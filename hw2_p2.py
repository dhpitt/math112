# David Pitt
# HW2, P2 exploration
from cobwebGenerator import plot_cobweb, AnnotatedFunction
import matplotlib.pylab as plt
import math
import numpy as np

funcB = AnnotatedFunction(lambda x: math.pi/2*np.cos(x), r'$\frac{\pi}{2}cos(x)$')

plot_cobweb(funcB,0.25,60,[-1,7])

funcC = AnnotatedFunction(lambda x: abs(x-2)-1, r'$|x-2|-1$')

#plot_cobweb(funcC,-0.25,60,[-3,3])
#plot_cobweb(funcC,0.0,0.25,60,[-3,3])
