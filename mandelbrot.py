# David Pitt
# Feb 15, 2021
# Generator of the mandelbrot set

import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
# This is mostly an excuse for me to learn Seaborn. 
# I've seen tons of pretty figures made in Seaborn, and my 
# MPL graphs always look kinda ugly. Hopefully this is a useful exercise!

def mandelbrot(z,c):
    return z^2+c

iter_limit = 81

def mandelbrot_Diverge(c,max_iters=iter_limit):
    # Returns the number of iterations 
    # an initial condition takes to diverge
    # up to a certain limit so that I don't break my laptop
    z = 0
    n = 0
    while abs(z) < 2 and n < max_iters:
        z = z**2 + c
        n += 1
    return n

#####################
# Draw the set in C #
#####################

res = 1200
df = np.zeros([res,res])
print(df.shape)

xmin = -2#-2
xmax = 1#1
ymin = -1#-1
ymax = 1#1
for n in range(res):
    for m in range(res):
        # n = column, m = row
        c = xmin+n/(res/(xmax-xmin)) + 1j*(ymin+(m/(res/(ymax-ymin))))
        df[m][n] = mandelbrot_Diverge(c)

sns.set_palette("husl")
ax = sns.heatmap(df,vmin=0,vmax=iter_limit)
plt.show()