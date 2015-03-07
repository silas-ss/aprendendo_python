#!/usr/bin/python
#-*- coding: latin-1 -*-

km = float(input('KM percorridos: '))
dias = int(input('Quantidade de dias alugado: '))

preco_pagar = km * 0.15 + dias * 60

print ('Preço a pagar: %.2f' %preco_pagar)

