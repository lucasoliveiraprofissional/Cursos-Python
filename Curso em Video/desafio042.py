'''Refaça o desafio 035 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado.

-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes'''

#Desafio 035b (Jeito fácil que o prof fez):
'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo'''

r1= float(input('Primeiro segmento: '))
r2= float(input('Segundo segmento: '))
r3= float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    #print('Os segmentos acima podem formar um triângulo!')
    #comentei só para deixar uma referencia ao programa antigo.

    #condição do tipo de triangulo:
    if r1 == r2 and r2 == r3:
        print('O triangulo formado será Equilátero.')
    elif (r1 == r2 and r2 != r3) or (r1 == r3 and r3 != r2) or (r2 == r3 and r3 != r1):
        print('O triangulo formado será Isósceles.')
    else:
        print('O triangulo formado será Escaleno.')

else:
    print('Os segmentos acima não podem formar um triângulo.')



