#!/usr/bin/python
# coding: latin-1

t = 0
for n in range(1067,3628):
    if n%2 == 0 and n%7 == 0:
       t = t + 1

print("%d são divisiveis por 2 e 7" %t)
