import matplotlib.pylab as plt
from matplotlib.pyplot import plot
import numpy as np
from numpy.lib.polynomial import polyint
from scipy.optimize import fsolve

def triangle(x):
    cond = np.random.randint(1,7)
    if cond == 1 or cond == 2:
        loc = np.array([0,0])
    elif cond == 3 or cond == 4:
        loc = np.array([1,0])
    elif cond == 5 or cond == 6:
        loc = np.array([0,1])

    r = loc - x
    x += 0.5*r
    return x

def IFS1(x):
    beta = 1/3
    #points = ([1/2,1/6],[1/2,1/2],[1/6,5/6],[5/6,5/6],[1/2,5/6])
    points = ([1/2,1/3],[1/2,2/3],[1/2,1],[1/6,1],[5/6,1])
    p_i = np.array(points[np.random.randint(0,5)])
    
    return beta*(x-p_i) + p_i
    #return x + beta*(p_i-x)
    

def IFS(x,points,beta):
    
    p_i = np.array(points[np.random.randint(0,len(points))])

    return p_i + beta*(x-p_i)


num_pts = 20000
attractor_length = 200
pos = []

pts = ([1/2,0],[1/2,1/3],[1/2,2/3],[2/3,1/6],[2/3,5/6])
pts1 = ([1/2,1/3],[1/2,2/3],[1/2,1],[1/6,1],[5/6,1])
pts2 = ([0,1],[1/3,1],[2/3,1],[1/2,1/3],[1/2,2/3])
ctr = ([1/2,1/6],[1/2,1/2],[1/2,5/6],[1/6,5/6],[5/6,5/6])
#outer2 = ([1/2,0],[1/2,1/2],[1/2,5/6],[0,1],[1,1])
points_1st = ([1/2,0],[1/2,1/2],[1/2,1],[0,1],[1,1])
cool_X_points = ([1/2,0],[0,1],[1,0],[1/2,1/2],[1/2,1])

for _ in range(num_pts):
    xI = np.array([0.5,0.5])
    for _ in range(attractor_length):
        xI = IFS(xI,cool_X_points,1/3)

    pos.append([xI[0],xI[1]])

ax = plt.subplot()
ax.set(xlim=[0,1],ylim=[0,1])
ax.set_title("End behavior of IFS")

slices = np.arange(0,1,100)
#ax.plot([0 for s in slices],slices)
#ax.plot()
ax.scatter([p[0] for p in pos],[p[1] for p in pos],s=2)


plt.show()

