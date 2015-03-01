#!/usr/bin/python
# -*- coding:latin-1 -*-

preco_mercadoria = float(input('Preço da mercadoria: '))
desconto = float(input('Percentual de desconto: '))

valor_desconto = preco_mercadoria * (desconto / 100)
novo_preco = preco_mercadoria - valor_desconto

print ('- Valor do desconto: %.2f\n= Preço a pagar: %.2f' %(valor_desconto, novo_preco))
