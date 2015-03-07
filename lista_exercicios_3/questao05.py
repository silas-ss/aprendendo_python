#!/usr/bin/python
# coding: latin-1

n1, n2 = int(input("Digite um número: ")), int(input("Digite um número: "))

r = 1
x, y = n1, n2
while r != 0:
   r = n1%n2
   if r != 0:
      n1, n2 = n2, r

print("O MDC de %d e %d é: %d" %(x,y,n2))
