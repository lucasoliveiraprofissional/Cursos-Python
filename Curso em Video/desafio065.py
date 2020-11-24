'''Crie um programa que leia vários números
inteiros. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor
valor lido. O programa deve perguntar ao usuário
se ele quer continuar ou não a digitar valores.'''

'''Eu quis fazer a média a cada execução.
Talvez isso esteja errado. Depois ajustei
isso para que não acontecesse a cada execução.'''


maior= 0
menor= 0
numero= 0
soma= 0
cont= 0

pergunta= 's'

while pergunta not in 'Nn':
    numero= int(input('Digite um numero inteiro: '))
    soma+= numero

    if cont == 0:
        maior= numero
        menor= numero

    else:
        if numero > maior:
            maior= numero

        if numero < menor:
            menor= numero

    cont+= 1

    pergunta= input('\nVocê quer continuar? [S/N]: ').upper()

print('\nA média dos números digitados é: {:.2f}'.format(soma / cont))
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))