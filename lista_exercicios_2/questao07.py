#!/usr/bin/python
# coding: latin-1

area = float(input("Digite a área a ser pintada(m²): "))

total_litros = area / 3
quantidade_latas = total_litros / 18
if quantidade_latas != int(quantidade_latas):
   quantidade_latas += 1

preco_total = quantidade_latas * 80;

print ("Quantidade de latas a serem compradas: %d\nPreço total: R$ %.2f" %(quantidade_latas, preco_total))
