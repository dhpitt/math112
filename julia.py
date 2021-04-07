# David Pitt
# Mar 22, 2021
# First generator of julia set animations

import numpy as np
import seaborn as sns
import math
import matplotlib.pylab as plt
from tqdm import tqdm
from matplotlib.animation import FuncAnimation
import matplotlib.animation as anim


iter_limit = 81

def julia(z,c,max_iters=iter_limit):
    # Returns the number of iterations 
    # an initial condition takes to diverge
    # up to a certain limit so that I don't break my laptop
    n = 0
    while abs(z) < 2 and n < max_iters:
        z = z**2 + c
        n += 1
    return n

#####################
# Draw the set in C #
#####################

resx = 300
resy = 200
res_c = 100
#df = np.zeros([resy,resx,res_c])
df = np.zeros([resy,resx])
print(df.shape)

x_offset = resx/2
y_offset = resy/2
one = resx/3
'''
for i in tqdm(range(res_c)):
    for n in range(resx):
        for m in range(resy):
            # n = rows, m = cols
            zx = (n - x_offset)/one
            zy = 1j * (m - y_offset)/one
            c = 0.7785*np.exp(1j*(6.28*i/res_c))
            df[m][n][i] = julia((zx+zy),c)
'''
for n in range(resx):
    for m in range(resy):
        # n = rows, m = cols
        zx = (n - x_offset)/one
        zy = 1j * (m - y_offset)/one
        #c = 0.7785*np.exp(1j*(6.28*i/res_c))
        df[m][n] = julia((zx+zy),0.64*1j)
        
fig,ax = plt.subplots()
#ax.imshow(df[:,:,0])
ax.imshow(df[:,:])
'''
def animateJuliaRotation(i):
    ax.imshow(df[:,:,i])

anim = anim.FuncAnimation(fig, animateJuliaRotation, frames=list(range(0,res_c)), \
                                      interval=100, blit=False, repeat=True)

ax.set(xlabel='Re(z)',ylabel='Im(z)')
ax.set(title='Julia set for ' + r'$p(z) = z^2 + 0.7785e^{i_\theta}$')
plt.draw()

'''
plt.show()
#anim.save('julia_anim_2.mp4', fps=35, extra_args=['-vcodec', 'libx264'])

#ax = sns.heatmap(df,vmin=0,vmax=iter_limit)
