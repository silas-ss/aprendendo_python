#!/usr/bin/python
# coding: latin-1

import random

lista = []
for c in range(0,10):
    lista.append(random.choice(range(1,101)))

menor = maior = lista[0]
for n in lista:
    if n > maior:
       maior = n
    if n < menor:
       menor = n

print("A lista é: ",lista)
print("O maior é %d e o menor é %d" %(maior,menor))
