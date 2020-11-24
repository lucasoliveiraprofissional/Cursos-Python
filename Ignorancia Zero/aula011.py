'''Pedir para o usuário digitar um valor de 1 a 7
são respectivos aos dias da semana
se o valor não for desses, o resultado é um print:
Entrada inválida

Ensinando If e elses aninhados

A variável que verifica se o dia é válido, fica verdadeira
a cada entrada certa feita.
'''

'''
Do primeiro modo:

dia= int(input('Digite o dia da semana: '))
verifica= False

if dia == 1:
    print('Domingo')
    verifica == True
if dia == 2:
    print('Segunda')
    verifica == True
if dia == 3:
    print('Terça')
    verifica == True
if dia == 4:
    print('Quarta')
    verifica == True
if dia == 5:
    print('Quinta')
    verifica == True
if dia == 6:
    print('Sexta')
    verifica == True
if dia == 7:
    print('Sábado')
    verifica == True

if verifica != True:
    print('Entrada inválida!') '''

'''Otimizado:'''

dia= int(input('Digite o dia da semana: '))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('Terça')
elif dia == 4:
    print('Quarta')
elif dia == 5:
    print('Quinta')
elif dia == 6:
    print('Sexta')
elif dia == 7:
    print('Sábado')

else verifica != True:
    print('Entrada inválida!')