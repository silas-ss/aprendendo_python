#!/usr/bin/python
# -*- codigin: latin-1 -*-

peso = float(input("Digite o peso de peixes: "))

excesso = 0
multa = 0
if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso

print ("Excesso: %.2f => Multa: R$ %.2f" %(excesso, multa))


