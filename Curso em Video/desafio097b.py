'''Faça um programa que tenha uma função
chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com
tamanho adaptável.'''

'''Fiz a versão b pois a proposta dele para esse 
exercício é bem diferente do que eu pensava,
pois já fui fazendo sem ver como exatamente
ele queria.'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#programa principal:
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')