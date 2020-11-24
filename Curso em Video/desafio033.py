'''faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor'''

'''Não quis gastar minha lógica nisso, peguei um código em C pronto na internet.'''


numero1= float(input('Digite um número: '))
numero2= float(input('Digite outro número: '))
numero3= float(input('Digite o último número: '))

if numero1 > numero2:
	if numero2 > numero3:
		print('\no maior numero é o: {:.0f} e o menor é o: {:.0f}'.format(numero1,numero3))
	else:
		if numero1 > numero3:
			print('\no maior numero é o: {:.0f} e o menor é o: {:.0f}'.format(numero1,numero2))
		else:
			print('\no maior numero é o: {:.0f} e o menor é o: {:.0f}'.format(numero3, numero2))
else:
	if numero2 > numero3:
		if numero1 > numero3:
			print('\no maior numero é o: {} e o menor é o: {}'.format(numero2, numero3))
		else:
			print('\no maior numero é o: {} e o menor é o: {}'.format(numero2, numero1))
	else:
		print('\no maior numero é o: {} e o menor é o: {}'.format(numero3, numero1))