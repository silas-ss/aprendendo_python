#!/usr/bin/python
# -*- coding: latin-1 -*-

l1 = float(input("Digite o valor lado A: "))
l2 = float(input("Digite o valor lado B: "))
l3 = float(input("Digite o valor lado C: "))

if l1 + l2 < l3 or l2 + l3 < l1 or l3 + l1 < l2:
    print ("Não é um triângulo!")
else:
   if l1 == l2 and l2 == l3:
       print ("Triâgulo equilátero!")
   elif (l1 == l2 and l2 != l3) or (l1 == l3 and l3 != l2) or (l3 == l2 and l1 != l2):
       print ("Triângulo isósceles!")
   else:
       print ("Triângulo escaleno!")

