# David Pitt
# Math 112, HW7

#p1
import matplotlib.pylab as plt
from matplotlib.pyplot import plot
import numpy as np


def IFS(x,points,beta):
    
    p_i = np.array(points[np.random.randint(0,len(points))])

    return p_i + beta*(x-p_i)


num_pts = 10000
attractor_length = 100
pos = []

pts = ([0,0],[1,0],[0,1],[1,1])

for _ in range(num_pts):
    xI = np.array([0.5,0.5])
    for _ in range(attractor_length):
        xI = IFS(xI,pts,1/3)

    pos.append([xI[0],xI[1]])

ax = plt.subplot()
ax.set(xlim=[0,1],ylim=[0,1])
ax.set_title("End Behavior of IFS")

slices = np.arange(0,1,100)
#ax.plot([0 for s in slices],slices)
#ax.plot()
ax.scatter([p[0] for p in pos],[p[1] for p in pos],s=2)


plt.show()