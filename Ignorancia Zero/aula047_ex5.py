"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar
M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.
"""


resp= input('Em qual turno você estuda?'
            '\n[M-matutino ou V-Vespertino ou N- Noturno]: ')

if resp == 'M' or resp == 'm':
    print('Bom Dia!')
elif resp == 'V' or resp == 'v':
    print('Boa Tarde!')
elif resp == 'N'or resp == 'n':
    print('Boa Noite')
else:
    print('Valor Inválido!')


