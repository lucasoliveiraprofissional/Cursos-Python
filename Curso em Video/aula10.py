#programa 1

'''nome= str(input('Qual é seu nome? '))

if nome == 'Gustavo':
	print('Esse é o seu nome!')
else:
	print('Seu nome é tão normal!')

print('Bom dia {}!'.format(nome))
'''

#programa 2

n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))

m= (n1 + n2)/2

if m>= 6.0:
	print('A sua média foi: {:.1f}'.format(m))
	print('Sua média foi boa! Parabéns!')
else:
	print('A sua média foi: {:.1f}'.format(m))
	print('Sua média foi ruim! Estude mais!')	