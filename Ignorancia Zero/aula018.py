'''Repetições encaixadas: '''

'''
for i in range(3):
    for j in range(3):
        print(i, j)
'''
'''Pedir para o usuário entrar com o início e o fim da tabuada
e imprima a tabuada correspondente dentro dos intervalos considerados
Exemplo: 
Começo = 1
Fim = 3

Para o 1:
1X1 = 1
1X2 = 2
1X3 = 3

Para o 2:
...'''

inicio= int(input('Digite o inicio da tabuada: '))
fim= int(input('Digite o fim da tabuada: '))

print('')
for i in range(inicio, fim+1):
    print('Para o {}: '.format(i))
    for j in range(inicio, fim+1):
        print('{}X{} = {}'.format(i, j, i*j))
    print('')
