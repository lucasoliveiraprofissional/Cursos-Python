"""
Escreva o jogo do chute.
Nele você deve sortear um número inteiro entre 1 e 100 e pedir
para o usuário advinhar o número que você escolheu

Para cada chute do usuário você deve imprimir uma dica, se
ele chutou baixo de mais ou alto demais

Uma vez que o usuário acerte o chute o programa imprime uma
mensagem e também o número de chutes que o usuário deu

OBS: Use o statement break

Exemplo:

>>>
Tente advinhar o número que eu estou pensando
Seu Chute: 50
Você deve chutar mais alto!
Seu Chute: 75
Você deve chutar mais alto!
Seu Chute: 87
Você deve chutar mais alto!
Seu Chute: 93
Você deve chutar mais alto!
Seu Chute: 97
Você deve chutar mais baixo!
Seu Chute: 95
Parabens você acertou!!
Você chutou 6 vezes
>>>

"""

from random import randint

def verificachute(num):
    global chute
    cont= 0

    while num < escolhido:
        print('Você deve chutar mais alto!')
        print(f'Seu chute: {num}')
        cont += 1
        chute = int(input('Digite o número desejado: '))


    while num > escolhido:
        print('Você deve chutar mais baixo!')
        print(f'Seu chute: {num}')
        cont += 1
        chute = int(input('Digite o número desejado: '))

    if num == escolhido:
        return num

while True:
    escolhido= randint(0, 10)

    chute= int(input('Digite o número desejado: '))

    n= verificachute()

    n(chute)

    if n:
        break
        print('Você acertou!')
        print(f'Voce chutou {cont} vezes')
