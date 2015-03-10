#!/usr/bin/python
# coding: latin-1

t = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone Our community is based on
mutual respect tolerance, and encouragement and we are working to help each other live up
to these principles We want our community to be more diverse: whoever you are and
whatever your background, we welcome you'''

lista = t.split()
lista2 = []

for p in lista:
    for l in 'python':
        if l in p.lower() and len(p) > 4:
           lista2.append(p)
           break

print(lista2)
