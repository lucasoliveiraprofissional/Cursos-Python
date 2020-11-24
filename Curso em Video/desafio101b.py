'''Crie um programa que tenha uma função chamada voto()
que vai receber como parametro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.'''

'''Fiz versão B só para ver como ele faria, o meu está certo.'''

def voto(ano):
    from datetime import date
    atual= date.today().year
    idade= atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

#programa principal:
nasc= int(input('Em que ano você nasceu? '))
print(voto(nasc))