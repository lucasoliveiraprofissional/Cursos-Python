'''Melhore o jogo DESAFIO 028 onde o computador
vai 'pensar' em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar,
mostrando no final quatos palpites foram necessários
para vencer.'''
'''Eu fui ver por curiosidade como o Gustavo fez
a primeira verificação se o usuário digitou certo.
Porém ele fez algumas coisas interessantes.
Eu decidi então pegar o código todo.'''

from random import randint
computador= randint(0, 10)

print('Será que voce consegue adivinhar? ')
print('')

#acertou está como false porque o usuário não
#fez nenhuma tentativa ainda.
acertou= False
palpite= 0

while not acertou:
    jogador= int(input('Qual é seu palpite? '))
    palpite+= 1
    if jogador == computador:
        acertou= True

    #só para falar se está perto ou longe:

    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')

print('Acertou! Foram {} palpites'.format(palpite))

