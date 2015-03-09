#!/usr/bin/python
# coding: latin-1

valor_conta = int(input("Digite o valor a ser pago: "))
valor_pago = int(input("Digite o valor pago: "))

troco = valor_pago - valor_conta
print("O valor do troco é: %d" %troco)
nota50 = nota20 = nota10 = nota5 = nota2 = nota1 = 0
if troco > 0:
   while troco > 0:
       if troco >= 50:
          nota50 = int(troco/50)
          troco = troco%50
       elif troco >= 20:
          nota20 = int(troco/20)
          troco = troco%20
       elif troco >= 10:
          nota10 = int(troco/10)
          troco = troco%10
       elif troco >= 5:
          nota5 = int(troco/5)
          troco = troco%5
       elif troco >= 2:
          nota2 = int(troco/2)
          troco = troco%2
       elif troco>= 1:
          nota1 = int(troco/1)
          troco = troco%1
if nota50 > 0:
   print("%d notas de R$ 50" %nota50)
if nota20 > 0:
   print("%d notas de R$ 20" %nota20)
if nota10 > 0:
   print("%d notas de R$ 10" %nota10)
if nota5 > 0:
   print("%d notas de R$ 5" %nota5)
if nota2 > 0:
   print("%d notas de R$ 2" %nota2)
if nota1 > 0:
   print("%d notas de R$ 1" %nota1)
