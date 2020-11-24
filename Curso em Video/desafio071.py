'''Crie um programa que simule o
funcionamento de um caixa eletronico.
No inicio pergunte ao usuário qual o
valor que será sacado(numero inteiro)
e o programa vai informar quantas
cédulas de cada valor serão entregues.

OBS.: Considere que o caixa possui
cédulas de R$50, R$20, R$10 e R$1'''

pergunta= ''

#while True:
valor= int(input('Digite qual o valor a ser sacado: '))

cinquenta= valor // 50
vinte= valor // 10
vinte= cinquenta - vinte


print(cinquenta)
print(vinte)