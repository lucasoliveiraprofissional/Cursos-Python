'''Crie um programa que tenha uma função chamada voto()
que vai receber como parametro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.'''

from datetime import datetime

def voto(num):
    idade= datetime.now().year - ano

    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO!')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')



ano= int(input('Em que ano você nasceu? '))
voto(ano)