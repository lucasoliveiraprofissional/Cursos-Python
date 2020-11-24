'''
Escreva um programa para testar o acerto entre 3 portas, trecho do filme quebrando a banca.
'''

import random

testes= int(input('Digite o número de testes: '))
trocar= 0
n_trocar= 0
#vai incrementar essas variaveis cada vez que for
#vantajoso trocar, ou que não for vantajoso trocar

for i in range(testes):
    #escolher a porta, entre 1 e 3
    porta= random.randrange(1, 4)
    premio= random.randint(1, 3)

    if porta == premio:
        n_trocar+= 1
    else:
        trocar+= 1

#nao vamos fazer como no jogo, onde o apresentador
#questiona se o usuario quer trocar a porta

print('É vantajoso trocar em {:.2f}% das vezes'.format(trocar*100/testes))
print('Não é vantajoso trocar em {:.2f}% das vezes'.format((1-trocar/testes)*100))

