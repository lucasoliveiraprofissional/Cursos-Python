'''Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário
digitar 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a
soma entre eles. (desconsiderando o flag)'''

num= 0
soma= 0

while num != 999:
    if num != 999:
        num= int(input('Digite um número inteiro: '))
        soma+= num

print('A soma dos números digitados é: {}'.format(soma))

