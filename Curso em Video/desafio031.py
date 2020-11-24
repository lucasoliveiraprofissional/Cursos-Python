''' faça um programa que pergunte a distância
de uma viagem em km. Calcule o preço da passagem,
cobrando R$0,50 por KM para viagens de até 200km,
e R$0,45 para viagens mais longas '''

'''nesse caso, o fato de eu calcular tudo no format atrapalhou um pouco, pois eu poderia ter reduzido
o número de frases que eu poderia colocar aqui nos prints'''

distancia= float(input('Digite a distância de sua viagem em Km: '))

if distancia <= 200:
	print('\nSua viagem custará: R${:.2f}'.format(distancia*0.5))
	print('Nessa quilometragem a taxa é de R$0,50/Km.')
else:
	print('\nSua viagem custará: R${:.2f}'.format(distancia*0.45))
	print('Nessa quilometragem a taxa é de R$0,45/Km.')