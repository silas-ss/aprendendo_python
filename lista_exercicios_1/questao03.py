dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

segundos += (minutos * 60) + (horas * (60 ** 2)) + (dias * (24 * (60 ** 2)))

print ('%d segundos' %segundos)
