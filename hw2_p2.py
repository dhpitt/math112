# David Pitt
# HW2, P2 exploration
from cobwebMaker import plot_cobweb, AnnotatedFunction
import matplotlib.pylab as plt
import math
import numpy as np

funcB = AnnotatedFunction(lambda x,r: math.pi/2*np.cos(x), r'$\frac{\pi}{2}cos(x)$')

#plot_cobweb(funcB,0.0,0.25,60,[-1,2*math.pi])
#plot_cobweb(funcB,0.0,-0.25,60,[-1,2*math.pi])

funcC = AnnotatedFunction(lambda x,r: abs(x-2)-1, r'$|x-2|-1$')

plot_cobweb(funcC,0.0,-0.25,60,[-3,3])
#plot_cobweb(funcC,0.0,0.25,60,[-3,3])
