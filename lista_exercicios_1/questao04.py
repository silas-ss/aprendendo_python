#!/usr/bin/python
# -*- coding: latin-1 -*-

salario = float(input('Salario: '))
aumento = float(input('Porcentagem do aumento: '))

valor_aumento = salario * (aumento / 100)
novo_salario = salario + valor_aumento

print ('+ Valor do aumento: %.2f\n = Novo salário: %.2f' %(valor_aumento, novo_salario))
