'''Faça um programa que leia 20 numeros inteiros e armazene-os num vetor.
Armaneze os numeros pares no vetor PAR e os numeros impares no vetor IMPAR.
Imprimir os 2 vetores depois.'''

par= []
impar= []
lista= []

for i in range(1, 3):
    num= int(input('Digite o numero {} de 20: '.format(i)))
    lista.append(num)

    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)

'''Fiz uma perfumaria, coloquei a lista de todos os numeros que foram digitados.
Depois  eu quis tirar os colchetes, porém para isso, precisei transformar a lista
em string e depois usar o método que tira os colchetes.
Fiz tudo no format, porém isso também poderia ser feito do seguinte modo:
lista= str(lista)
lista= lista.strip('[]')

ou:

lista= lista.str(lista).strip('[]')
e depois só dou um format(lista) nesse caso.
'''

print('')
print('Os numeros digitados foram: \n{}\n'.format(str(lista).strip('[]')))
print('Entre eles, os numeros pares digitados foram: \n{}\n'.format(str(par).strip('[]')))
print('Entre eles, os numeros impares digitados foram: \n{}'.format(str(impar).strip('[]')))