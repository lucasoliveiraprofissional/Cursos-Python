'''listas dentro de listas, adicionar novos elementos a listas(append)'''

#lista dentro de outra
#lista= [1,2,3,4,[1,2,3,4]]

#obter um dos elementos de uma lista assim:
#lista[4][2]

#criando várias listas dentro de uma:
#lista= [[[1, 2], [3, 4]], [5, 6]]

#lista[0] é [[1, 2], [3, 4]]
#lista[1] é [5, 6]
#lista[0][0] é [1, 2]
#lista[0][0][0] é 1
#lista[0][1][1] é 4

#lista += lista[0]
#= [[[1, 2], [3, 4]], [5, 6], [1, 2], [3, 4]]

#lista de tamanho n:

'''Faça um programa que leia um vetor de 5 numeros inteiros e mostre-os'''

#vetor é uma lista vazia
vetor= []
for i in range(1, 6):
    num= int(input('Digite o numero {} de 5: '.format(i)))
    vetor.append(num)
    #assim conseguimos inserir um valor dentro do vetor, vai como parametro
    #da funcao append o valor que o usuario for digitar, o valor que é incrementado
    #no for ou o valor que quisermos.

print(vetor)

'''Método append acrescenta elementos depois do último elemento existente na lista.
Caso não haja nenhum, o elemento que será adicionado irá ao indice 0 da lista.'''