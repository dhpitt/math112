# Generates cobweb diagrams using
# iterations of an annotated function object.
# I adapted this code from SciPython.com's 
# Cobweb Plots blog post and added functionality
# to handle more classes of functions.

import matplotlib.pylab as plt
from matplotlib import rc
import numpy as np
import math

dpi = 72

def plot_cobweb(f, x0, nmax=40, X=[0,1], res=500):
    """ Makes a cobweb diagram.
    Plot y = f(x) and y = x for the subspace X, and 
    illustrate the long-term behavior of f(x) starting 
    at x = x0. r is a parameter to the function.
    """
    x = np.linspace(X[0], X[1], res+1) 
    fig = plt.figure(figsize=(600/dpi, 450/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    # Plot y = f(x) and y = x
    ax.plot(x, [f(i) for i in x], c='#444444', lw=2)
    ax.plot(x, x, c='#444444', lw=2)

    # Iterate x = f(x) for nmax steps, starting at (x0, 0).
    px, py = np.empty((2,nmax+1,2))
    px[0], py[0] = x0, 0
    for n in range(1, nmax, 2):
        px[n] = px[n-1]
        py[n] = f(px[n-1])
        px[n+1] = py[n]
        py[n+1] = py[n]

    # Plot the path traced out by the iteration.
    ax.plot(px, py, c='b', alpha=0.7)

    # Annotate and tidy the plot.
    ax.minorticks_on()
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel('$x$')
    ax.set_ylabel(f.latex_label)
    ax.set_title('$x_0 = {:.01}$'.format(x0))
    plt.show()
    #plt.savefig('cobweb_{:.1}_{:.2}.png'.format(x0, r), dpi=dpi)

class AnnotatedFunction:
    """A small class representing a mathematical function.

    This class is callable so it acts like a Python function, but it also
    defines a string giving its LaTeX representation.

    """

    def __init__(self, func, latex_label):
        self.func = func
        self.latex_label = latex_label

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

