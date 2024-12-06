lista = [float(input()) for x in range(3)]
if sorted(lista)[0] + sorted(lista)[1] > sorted(lista)[2]:
	if lista[0] == lista[1] and lista[0] == lista[2] and lista[1] == lista[2]:
		print('o seu triangulo existe e equilatero')
	elif lista[0] == lista[1] or lista[0] == lista[2] or lista[1] == lista[2]:
		print('o seu triangulo existe e isosceles!')
	else:
		print('o seu triangulo existe e escaleno!')
else:
	print('o seu triangulo nao existe!')