import numpy as np
import matplotlib.pylab as plt

# problem 2
def g4(x):
    for i in range(4):
        x = 3.5*x*(1-x)
    return x

n = list(range(1000))

n = np.divide(n,100)

g4_list = []
for i in n:
    g4_list.append(g4(i))

ax = plt.subplot()
ax.set(xlim=(0,1),ylim=(0,1))

ax.plot(n,g4_list)
ax.plot(n,n)
plt.show()

# Sweep the lines to find points of period 4
#points = []
'''
func_string = "(3.5*x*(1-x))"

g4 = func_string

for i in range(4):
    g4 = g4.replace("x",func_string)

print(g4)k
'''

# Create the orbits for P2
points = [0,0.383,0.428,0.500,0.714,0.828,0.857,0.873]

for point in points:
    orbit = []
    x = point
    for i in range(5):
        orbit.append(x)
        x = 3.5*x*(1-x)
    print(orbit)