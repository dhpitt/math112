# David Pitt
# HW7 Project
# Mar 28, 2021

import matplotlib.pylab as plt
from matplotlib.pyplot import plot
import numpy as np


def IFS(x,points,beta):
    
    p_i = np.array(points[np.random.randint(0,len(points))])

    return p_i + beta*(x-p_i)


def twoD_Mat_IFS(x,points,betas,As):
    #A_i = np.array([[beta+1,0],[0,beta]])
    ind = np.random.randint(0,len(points))
    p_i = np.multiply(betas[ind],np.array(points[ind]))
    return np.matmul(np.array(As[ind]),x)+p_i



num_pts = 20000
attractor_length = 200
pos = []

# A_i lists
A_list_1 = [[[1/3,0],[1/2,0]],[[1/3,0],[1/2,0]],[[1/3,0],[1/2,0]]] # odd collection of lines, attractor
A_list_2 = [[[1/3,3],[1/5,7/10]],[[1/3,0],[1/2,2/3]],[[1/4,3/5],[1/2,1/6]]]


# Beta lists
betas_1 = (1/2,1/3,1/4)
betas_2 = (1,1,1)

triangle = ([0,0],[0,1],[1,0])
pts = ([1/2,0],[1/2,1/3],[1/2,2/3],[2/3,1/6],[2/3,5/6])
pts1 = ([1/2,1/3],[1/2,2/3],[1/2,1],[1/6,1],[5/6,1])
pts2 = ([0,1],[1/3,1],[2/3,1],[1/2,1/3],[1/2,2/3])
ctr = ([1/2,1/6],[1/2,1/2],[1/2,5/6],[1/6,5/6],[5/6,5/6])
#outer2 = ([1/2,0],[1/2,1/2],[1/2,5/6],[0,1],[1,1])
points_1st = ([1/2,0],[1/2,1/2],[1/2,1],[0,1],[1,1])
cool_X_points = ([1/2,0],[0,1],[1,0],[1/2,1/2],[1/2,1])
ptsOutside = ([3,0],[0,-2],[2,0],[1/2,4],[4,-1])

for _ in range(num_pts):
    xI = np.array([0.5,0.5])
    for _ in range(attractor_length):
        #xI = IFS(xI,ctr,1/3)
        xI = twoD_Mat_IFS(xI,triangle,betas_2,A_list_2)

    pos.append([xI[0],xI[1]])

ax = plt.subplot()
#ax.set(xlim=[0,1],ylim=[0,1])
ax.set_title("End behavior of IFS")

slices = np.arange(0,1,100)
#ax.plot([0 for s in slices],slices)
#ax.plot()
ax.scatter([p[0] for p in pos],[p[1] for p in pos],s=2)


plt.show()

