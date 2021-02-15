# David Pitt
# Feb 8 2020
# Module 4: Bounded Orbits and Fractal Dimensions
# Exploration

import numpy as np
import math
from cobwebGenerator import AnnotatedFunction, plot_cobweb
import matplotlib.pylab as plt

def TentMap(a,x):
    if x <= 1/2:
        return a*x
    else: 
        return a - a*x

def iterate(a,x,n):
    for _ in range(n):
        x = TentMap(a,x)
    return x