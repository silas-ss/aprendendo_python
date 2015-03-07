#!/usr/bin/python
# coding: latin-1
popa = 80000
popb = 200000
anos = 0

while popa < popb:
  if popa >= popb:
     break
  else:
     anos += 1
  popa = popa + (popa * 0.03)
  popb = popb + (popb * 0.015)

print("Em %d anos o país A terá a população maior ou igual a B" %anos)
