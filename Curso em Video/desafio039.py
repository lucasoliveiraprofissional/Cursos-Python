'''Faça um programa que leia o ano de nascimento de um
jovem e informe, de acordo com sua idade:

-Se ele ainda vai se alistar no serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta
ou que passou do prazo.'''

ano= int(input('Digite seu ano de nascimento: '))
idade= 2019-ano

if idade < 18:
    print('Você ainda vai se alistar.')
    print('Falta(m) {} ano(s)'.format((idade-18)*-1))
                                            #o *-1 é porque nesse caso essa conta sempre dará o
                                            #resultado esperado, porém negativo. Isso transforma
                                            #o número obtido em positivo.
elif idade == 18:
    print('Já é a hora de se alistar.')

else:
    print('Já passou do tempo de se alistar.')
    print('Passaram-se(ou-se) {} ano(s)'.format(idade-18))

