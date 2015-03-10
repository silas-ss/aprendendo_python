#!/usr/bin/python
# coding: latin-1

import random

lista = []
for c in range(0,20):
    lista.append(random.choice(range(1,101)))

par = []
impar = []
for n in lista:
    if n%2 == 0:
       par.append(n)
    else:
       impar.append(n)

print("Lista: ",lista)
print("Par: ",par)
print("Impar: ",impar)
