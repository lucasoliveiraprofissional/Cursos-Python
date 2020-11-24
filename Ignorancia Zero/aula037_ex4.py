'''Escreva uma função que gera uma matriz 4x4 com os números de 0 a 15 sem repetições'''

import random
matriz= []

def geramatriz(matriz):
    lista= list(range(16))
    for j in range(4):
        linha= []
        for i in range(4):
            x= random.choice(lista)
            #dentro da lista que contem os elemendos de range 0 a 15, ele escolherá um desses numeros
            #e atribuirá a x
            linha.append(x)
            lista.remove(x)
            #ele vai remover os elementos que já foram sorteados para que não haja repetições

            #no fim desse for, a linha estará com 4 elementos sorteados e a lista estará
            #com 4 elementos a menos.
            #isso faz com que a matriz tenha que atribuir a linha inteira com 4 elementos de uma vez só
            #e não ficar atribuindo cada elemento a cada laço de for

        matriz.append(linha)

#esse processo será feito 3 vezes, gerando 3
#matrizes diferentes com numeros randomicos não repetidos

#depois que cada matriz é gerada, ela é esvaziada, porque
#reaproveitamos a matriz para a próxima iteração

for i in range(3):
    matriz= []
    geramatriz(matriz)
    print(matriz)

