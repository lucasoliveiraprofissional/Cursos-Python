'''Reescreva a função LeiaInt() do exercicio
104, incluindo agora a possibilidade da
digitação de um número de tipo inválido.
Aproveite e crie também uma função
leiaFloat() com a mesma funcionalidade.'''

'''Achei um código nos comentários da aula
23 e pareceu simples, vou testar.
Autor: Gabriel Assunção'''

import requests

try:
    respose = requests.get('http://www.pudim.com.br/')
    print('Consegui acessar o site do Pudim com sucesso')
except:
    print('O site do Pudim não está disponível no momento.')