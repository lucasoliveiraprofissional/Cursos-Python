'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo'''

''' fórmula da existencia de um triangulo:
| b - c | < a < b + c 
| a - c | < b < a + c 
| a - b | < c < a + b '''


a= int(input('Digite o tamanho da primeira reta: '))
b= int(input('Digite o tamanho da segunda reta: '))
c= int(input('Digite o tamanho da terceira reta: '))

if (b - c) < a and a < (b + c):
    print('\nÉ possível formar um triângulo com esses valores')
else:
    if (a - c) < b and b < (a + c):
        print('\nÉ possível formar um triângulo com esses valores')
    else:
        if (a - b) < c and c < (a + b):
            print('\nÉ possível formar um triângulo com esses valores')
        else:
            print('\nNão é possível formar um triângulo com esses valores')