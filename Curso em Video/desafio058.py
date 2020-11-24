'''Melhore o jogo DESAFIO 028 onde o computador
vai 'pensar' em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar,
mostrando no final quatos palpites foram necessários
para vencer.'''

from random import randint

computador= randint(0, 10)
print('Pensei no número {}'.format(computador))
#revela o número que o computador pensou.

tentativa= 0


jogador = int(input('Em que número eu pensei? '))
if jogador != computador:
    tentativa+= 1

while jogador != computador:
    jogador = int(input(' Em que número eu pensei? '))
    tentativa+= 1

print('Agora acertou! O número de tentativas até acertar é: {} tentativas'.format(tentativa-1))

