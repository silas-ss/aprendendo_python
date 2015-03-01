#!/usr/bin/python
# -*- coding: latin-1 -*-

ganho_hora = float(input("Quanto você ganha por hora: "))
horas_mes = int(input("Número de horas trabalhadas no mês: "))

salario_bruto = ganho_hora * horas_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print ("+ Salário Bruto: R$ %.2f" %salario_bruto)
print ("- IR(11%%): R$ %.2f" %ir)
print ("- INSS(8%%): R$ %.2f" %inss)
print ("- Sindicato(5%%): R$ %.2f" %sindicato)
print ("= Salário Liquido: R$ %.2f" % salario_liquido)
