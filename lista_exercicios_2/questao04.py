#!/usr/bin/python
# -*- coding: latin-1 -*-

maior = 0
cont = 0

while cont < 3:
    n = int(input("Digite o %d° número: " %(cont + 1)))
    if cont == 0:
        maior = n
    if n > maior:
        maior = n
    cont += 1

print ("O maior número é %d!" %maior)
