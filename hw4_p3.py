# David Pitt
# Feb 18, 2021
# HW4, Problem 3

import numpy as np
import math
from cobwebGenerator import AnnotatedFunction, plot_cobweb
import matplotlib.pylab as plt
from scipy.optimize import fsolve

def h(x,c):
    if x <= 1/4:
        return c*x
    else:
        return c/3*(1-x)

def iterator(c,x,n):
    for _ in range(n):
        x = h(c,x)
    return x

h3 = AnnotatedFunction(lambda x: h(x,3), r'$h_c(x)$',)
sx = AnnotatedFunction(lambda x: np.sin(x), r'$sin(x)$',)
#plot_cobweb(sx,0.2)
plot_cobweb(h3,0.2)
plot_cobweb(h3,0.6)