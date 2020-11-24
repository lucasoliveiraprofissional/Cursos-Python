'''Escreva uma função que recebe um inteiro m e outro inteiro n e com isso
constroi uma matriz mxn'''

matriz= []
m= int(input('Digite o número de linhas da matriz: '))
n= int(input('Digite o número de colunas da matriz: '))

def constroimatriz(m, n, matriz):
    for i in range(1, m+1):
        linha= []
        for j in range(1, n+1):
            x= int(input('Digite o elemento {} {} da matriz: '.format(i, j)))
            linha.append(x)

        matriz.append(linha)

constroimatriz(m, n, matriz)

print(matriz)
