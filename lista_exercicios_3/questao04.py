#!/usr/bin/python
# coding: latin-1

n = int(input("Digite o número: "))

fib = fiba = 1

for c in range(3,n+1):
    fib, fiba = (fib + fiba), fib

print("O número Fibonacci de %d é: %d" %(n,fib))
