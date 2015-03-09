#!/usr/bin/python
# coding: latin-1

def primo(n):
    for c in range(2,n):
        if n%c == 0:
           return False
    return True

n = int(input("Digite um número: "))
if primo(n):
   print("%d é primo!" %n)
else:
   print("%d não é primo!" %n)
