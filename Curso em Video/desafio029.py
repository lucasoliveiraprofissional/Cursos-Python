'''escreva um programa que leia a velocidade de um carro
se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
multado. A multa vai custar R$7,00 por cada km acima do limite'''

velocidade= int(input('Digite somente o número de sua velocidade: '))

if velocidade > 80:
	print('\nVocê foi multado em: R${},00'.format((velocidade-80)*7))
print('\nTenha um bom dia! Dirija com segurança!')