'''fazer um programa que leia um ano qualquer e informe se ele é bissexto'''
''' A instrução if verifica se o ano é um múltiplo de 4, mas não é um múltiplo 
de 100 ou se é um múltiplo de 400 (nem todo ano que é um múltiplo de 4 é um ano bissexto). '''


ano= int(input('Digite um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('\nEsse ano é bissexto.')
else:
	print('\nEsse ano não é bissexto.')