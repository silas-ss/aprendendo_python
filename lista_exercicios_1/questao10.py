#!/usr/bin/python
#-*- coding: latin-1 -*-

cigarros_dia = int(input('Cigarros por dia: '))
anos_fumando = int(input('Anos fumando: '))

total_cigarros = cigarros_dia * (anos_fumando * 365)
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / (24 * 60)

print ('Dias perdidos fumando: %d' %dias_perdidos)
