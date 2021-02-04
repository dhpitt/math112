# David Pitt
# Module 3 Exploration
# and in-class activity Feb.2

# Finds long-term behaviors of the function
# h(x) = x^2 - 1

import matplotlib.pyplot as plt
import numpy as np

def h(x):
    return x**2 - 1

sweep = list(range(-100,100,1))
sweep = np.divide(sweep,100)
h100 = []
'''
for i in sweep:
    x = i
    orbit = []
    for j in range(3):
        x = h(x)
        x.append(orbit)
    h100.append(orbit)
'''

def orbit(x,n):
    o = []
    for i in range(n):
        o.append(x)
        x = h(x)
    return o

o0 = orbit(0,100)
o1 = orbit(1,100)
o2 = orbit(-0.75,100)
o3 = orbit(0.5,100)
o4 = orbit(1.618,100)

ax = plt.subplot()
#ax.plot(sweep,h100)
#ax.plot(sweep,sweep)
#ax.plot(o0, list(range(100)))
#ax.plot(o1,list(range(100)))
#ax.plot(o2,list(range(100)))
#ax.plot(o3,list(range(100)))
ax.plot(o4,list(range(100)))
plt.show()