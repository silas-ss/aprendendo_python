#!/usr/bin/python
# coding: latin-1

import random

l1 = []
l2 = []
li = []

for c in range(0,10):
    n = random.choice(range(1,100))
    l1.append(n)
    li.append(n)
    
    n = random.choice(range(1,100))
    l2.append(n)
    li.append(n)

print("Lista I: ",l1)
print("Lista II: ",l2)
print("Lista: ",li)


