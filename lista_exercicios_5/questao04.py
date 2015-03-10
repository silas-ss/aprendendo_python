#!/usr/bin/python
# coding: latin-1

t = 0
for n in range(18644, 33088):
    if '2' in str(n) and not '7' in str(n):
        t = t + 1

print("%d sortudos entre 18644 e 33087" %t)
