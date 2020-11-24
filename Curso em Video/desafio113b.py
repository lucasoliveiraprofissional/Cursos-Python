'''Reescreva a função LeiaInt() do exercicio
104, incluindo agora a possibilidade da
digitação de um número de tipo inválido.
Aproveite e crie também uma função
leiaFloat() com a mesma funcionalidade.'''

'''As coisas que ele quis fazer com as funções
ainda estão muito abstratas para que eu faça do 
zero, fiz a versão b por isso.'''

def leiaInt(msg):
    ok= False
    valor= 0
    while True:
        n= str(input(msg))

        if n.isnumeric():
            valor= int(n)
            ok= True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

def leiaFloat(msg):
    ok= False
    valor= 0
    while True:
        n= str(input(msg))

        if n.isnumeric():
            valor= float(n)
            ok= True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


try:
    n= leiaInt('Digite um número: ')

except TypeError:
    print('Você digitou um número do tipo inválido!')
else:
    print(f'Você acabou de digitar o número {n}')


try:
    n= leiaFloat('Digite um número: ')

except TypeError:
    print('Você digitou um número do tipo inválido!')
else:
    print(f'Você acabou de digitar o número {n}')