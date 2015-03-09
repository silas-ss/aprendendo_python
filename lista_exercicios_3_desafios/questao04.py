#!/usr/bin/python
# coding: latin-1

def primo(n):
    for c in range(2,n):
        if n%c == 0:
           return False
    return True

def somatorio(lista):
    t = 0
    for c in lista:
       t += c
    return t

n = int(input("Digite um número: "))
lista = []

for f in range(2,n):
    if primo(f):
       if n%f == 0:
          lista.append(f)

    if somatorio(lista) == n:
       break

print(n," decomposto é: ",lista)
