# David Pitt
# Math 112 HW2 P1
# Uses SciPy's fsolve (a Newton's method solver)
# to find the roots of g^4(x)-x (fixed points of the 4th iterate)

import matplotlib.pylab as plt
import numpy as np
from scipy.optimize import fsolve

def g4(x):
    return 4*x*(1-x)

def fourthIterate(x):
    for _ in range(4):
        x = g4(x)
    return x

def roots_fourth(x):
    return fourthIterate(x)-x
def iterate(x,n=4):
    for _ in range(n):
        x = g4(x)
    return x


slices = list(range(1001))
slices = np.divide(slices,1000)

ax = plt.subplot()
ax.plot(slices,slices)
ax.plot(slices,[fourthIterate(i) for i in slices],label='4')
ax.plot(slices,[iterate(i,3) for i in slices],label='3')
ax.plot(slices,[iterate(i,2) for i in slices],label='2')

ax.legend()

deltaFour = [[fourthIterate(i), fourthIterate(i)-i] for i in slices]

#pointsFour = []
#for i in deltaFour:
    #if abs(i[1]) <= 0.00775:
        #pointsFour.append(i[0])

#print([round(p,4) for p in pointsFour])
#print(len(pointsFour))


deltaTwo = [[iterate(i,2), iterate(i,2)-i] for i in slices]
deltaThree = [[iterate(i,3), iterate(i,3)-i] for i in slices]

pointsTwo = []
for i in deltaTwo:
    if abs(i[1]) <= 0.00775:
        pointsTwo.append(i[0])
pointsTwo = [round(p,4) for p in pointsTwo]

pointsThree = []

for i in deltaThree:
    if abs(i[1]) <= 0.00775:
        pointsThree.append(i[0])
pointsThree = [round(p,4) for p in pointsThree]

pointsFour = []
for i in deltaFour:
    if abs(i[1]) <= 0.00775:
        pointsFour.append(i[0])

guesses = list(range(30))
guesses = np.divide(guesses,29)
period_4_points = set()
for i in guesses:
    # fsolve returns an ndarray, index 0 is float
    period_4_points.add(fsolve(roots_fourth,i)[0]) 

rounded4 = [round(i,4) for i in period_4_points]
rounded4 = set(rounded4)
rounded4 = list(rounded4)
rounded4 = sorted(rounded4)
rounded4.remove(rounded4[6]) # this is a point that's equidistant from 2 fixed points
ax.scatter(rounded4,rounded4,color='red')

print("Points of period 4: " + str(rounded4))

min4 = rounded4
min4.remove(min4[0])
min4.remove(min4[5])
min4.remove(min4[9])
min4.remove(min4[11])
print("Minimal points of period 4: " + str(min4))
#print([round(p,4) for p in pointsFour])
#print(pointsThree)
#print(pointsTwo)
#print(len(pointsFour))

plt.show()

