#!/usr/bin/python
# coding: latin-1

def triangular(n):
    for c in range(1,10):
       if c*(c+1)*(c+2) == n:
           return True
       if (c+1) > 9 or (c+2) > 9:
           return False

n = int(input("Digite um número: "))
if triangular(n):
   print("%d é um número triangular!" %n)
else:
   print("%d não é um número triangular!" %n)

