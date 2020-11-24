'''Crie um programa onde 4 jogadores
joguem um dado e tenham resultados
aleatórios. Guarde esses resultados
em um dicionário. No final, coloque
esse dicionário em ordem, sabendo
que o vencedor tirou o maior número
no dado.'''

'''Fiz versão B pois vacilei, 
demorei para praticar python'''

from random import randint
from time import sleep
from operator import itemgetter

jogo= {'jogador1': randint(1, 6),
       'jogador2': randint(1, 6),
       'jogador3': randint(1, 6),
       'jogador4': randint(1, 6),}

'''Precisamos das informações em ordem.
Para isso, faz-se necessário a criação
de um outro dicionário.(ranking)'''

ranking= list()

'''Posteriormente, é usado o sorted, porém
o sorted trata com listas, não dicionarios
na hora de printar o resultado. Para isso
teremos que definir o ranking como lista,
não como dicionario.'''

print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

'''A posição 0 seria o nome jogador
e a posição 1 seria o numero sorteado.'''
'''Para mostrar o numero sorteado, ou 
qualquer item dentro de um dicionario,
precisamos usar um módulo chamado item
getter'''

ranking= sorted(jogo.items(), key= itemgetter(1), reverse=True)

print('\nResultado: ')
'''Usaremos o enumerate, pois não estamos
mais lidando com dicionarios nesse momento,
estamos lidado com listas'''

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)

