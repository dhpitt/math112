# David Pitt
# Mathematical Magician Solver

import matplotlib.pylab as plt
import numpy as np
import random

init_deck = list(range(1,18))
init_deck.reverse()

def split(deck):
    stacks = [[],[],[]]
    for i in deck:
        stacks[i%3].append(i)
    return stacks

def merge(stack,loc):
    # Shuffles the deck according to
    # which column has your card
    final = []
    final = final + stack[loc]
    if len(stack[(loc+1)%3]) > len(stack[(loc+2)%3]):
        final = stack[(loc+1)%3] + final + stack[(loc+2)%3]
    else: 
        final = stack[(loc+2)%3] + final + stack[(loc+1)%3]
    return final

# sp = split(init_deck)
# print(sp)
# mer = merge(sp,1)
# print(mer)

#def f(n,deck,iters):
def f(n,deck):
    # The same thing, but only takes n as input
    stacks = split(deck)
    i = 0
    for stack in stacks:
        if n in stack:
            i = stacks.index(stack)
    deck = merge(stacks,i)
    return deck.index(n),deck

#print(init_deck)
#print(f(5,init_deck))

ax = plt.subplot()
#ax.set(xlim=[0,18],ylim=[0,18])

#ax.plot(init_deck,init_deck)
#ax.plot(init_deck,[f(i,init_deck)[0] for i in init_deck])
shuff_1 = [f(i,init_deck)[1] for i in init_deck]
#print(shuff_1)
#ax.plot(init_deck,[f(f(i,init_deck)[0],shuff_1[i-1]) for i in init_deck])
for i in init_deck:
    x1,d1 = f(i,init_deck)
    x2,d2 = f(x1,d1)
    x3,d3 = f(x2,d2)
    x4,d4 = f(x3,d3)
    x5,d5 = f(x4,d4)
    x6,d6 = f(x5,d5)
    #print([i,x1,x2,x3,x4,x5,x6])
    #ax.plot([i,x1,x2,x3,x4,x5,x6],list(range(7)))
    
def numericalF(n):
    return 6+np.floor((17-n)/3)

def generalNF(n,d):
    return(np.ceil(d/3)+np.floor((d-n)/3))

def gnf2(n,d,o):
    return(np.ceil((2*d-n+o)/3))

correct_offsets = []
for i in init_deck:
    for o in range(-3,4):
        if f(i,init_deck)[0] == gnf2(i,17,o):
            correct_offsets.append([i,o])

#print(correct_offsets)

#print([[i,f(i,init_deck)[0]] for i in init_deck])
#print([[i,gnf2(i,17,-1)] for i in init_deck])
#ax.plot(init_deck,init_deck) # y = x

#ax.plot([numericalF(i) for i in init_deck],init_deck) # y = f(x) discrete
slices = list(range(171))
slices = np.divide(slices,10)
#ax.plot(slices,slices)
#ax.plot(slices,[numericalF(i) for i in slices]) # y = f(x) closer to continuous

#print([numericalF(i) for i in slices])
#ax.set(xlim=[0,20],ylim=[0,20])

another_deck = list(range(1,20))
#ax.plot(another_deck,another_deck)
#ax.plot(another_deck,[f(i,another_deck)[0] for i in another_deck])
#plt.show()
#print(nf2(10,17))

# Sweep to find working decks

#for i in range(17,26):
def getAttractor(i):
    attractors = []
    for j in range(1,i+1):
        att = [j]
        for k in range(8):
            att.append(gnf2(att[k],i,-1))
        attractors.append(att)
    return attractors

twenty = getAttractor(18)
for i in twenty:
    ax.plot(i,list(range(9)))

plt.show()


bad_decks = []
for i in range(1,52):
    for j in range(i):
        sample = getAttractor(i)[j]
        if sample[3] != sample[5] and i not in bad_decks:
            bad_decks.append(i)

print(bad_decks)





