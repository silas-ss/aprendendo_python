#!/usr/bin/python
# -*- coding: latin-1 -*-

maior = 0
menor = 0
cont = 0

while cont < 3:
    n = int(input("Digite o %d° número: " %(cont + 1)))
    if cont == 0:
        menor = n
        maior = n

    if n > maior:
        maior = n
    
    if n < menor:
        menor = n

    cont += 1

print ("O maior número é %d e o menor é %d!" %(maior, menor))
