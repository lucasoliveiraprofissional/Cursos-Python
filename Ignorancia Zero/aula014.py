#whiles encadeados

'''Exemplo inicial
i= 0
n= 5
j= 0

while i < n:
    while j < n:
        print(j)
        j= j + 1
    print(i)
    i= i + 1
'''

'''Dado um numero n de empresas, e um numero m de meses, e o ganho e 
gastos positivos e inteiros de cada empresa para cada mes,
imprimir se a empresa nesses meses ficou com déficit, lucro ou
indiferente e imprimir o valor correspondente a essa balança'''

'''Exemplo de execução:

Digite o numero de empresas: 3
Digite o número de meses: 2

Empresa 1: 
Mes 1:
Digite o ganho da empresa no mes: 500
Digite o gasto da empresa no mes: 500

Mes 2:
Digite o ganho da empresa no mes: 600
Digite o gasto da empresa no mes: 600

A empresa 1 ficou indiferente (balança = R$ 0)

Empresa 2:

...
'''

print('')
n= int(input('Digite o numero de empresas: '))
m= int(input('Digite o numero de meses: '))

empresa= 1
while empresa <= n:
    mes = 1
    balanca= 0
    print('Empresa {}:'.format(empresa))
    while mes <= m:
        print('Mes: {}:'.format(mes))
        ganho= int(input('Digite o ganho da empresa no mes: '))
        gasto= int(input('Digite o gasto da empresa no mes: '))
        balanca= balanca + (ganho - gasto)
        print('')
    #para que o while continue, é necessário incrementar as variaveis:
        mes = mes + 1



    #if para ver se a empresa está em débito, crédito ou indiferente:
    if balanca == 0:
        print('A empresa {} ficou indiferente(balança = R$ 0)'.format(empresa))
    elif balanca > 0:
        print('A empresa {} ficou com um lucro de R$ {}'.format(empresa, balanca))
    else:
        print('A empresa {} ficou com uma dívida de R$ {}'.format(empresa, balanca))

    empresa = empresa + 1