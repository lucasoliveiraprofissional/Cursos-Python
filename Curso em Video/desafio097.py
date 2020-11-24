'''Faça um programa que tenha uma função
chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com
tamanho adaptável.'''

'''Ex: 
escreva('Olá,Mundo!')

Saída:
------------
 Olá,Mundo!
------------'''

def escreva(texto):
    tamanho= len(escreva(texto) + 2)
    #print(f'-' * tamanho)
    #print('{:^tamanho}'.format(texto))

    print(f'{texto:^tamanho}')
    print(f'-' * tamanho)

escreva('Qualquer coisa.')


'''Trecho da aula 07a para me basear na centralização de strings:'''
'''print('Prazer em te conhecer {:=^20}!'.format(nome))'''
# faz o mesmo, mas alinhando o nome de acordo com os 20 caracteres,
# o nome ficará no centro e aos lados será preenchido com =

