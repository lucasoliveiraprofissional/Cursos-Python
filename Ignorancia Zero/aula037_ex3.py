'''Escreva uma função que troca um elemento por outro numa matriz'''

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

#vai receber uma tupla da posição 1 e da posição 2
#linha e coluna do elemento 1 e linha e coluna do elemento2
def trocaelemento(pos1, pos2, matriz):
    #[0] é linha e [1] é coluna
    elemento1= matriz[pos1//10-1][pos1%10-1]
    elemento2= matriz[pos2//10-1][pos2%10-1]

    #fazendo a troca:
    matriz[pos1//10-1][pos1%10-1]= elemento2
    matriz[pos2//10-1][pos2%10-1]= elemento1

#esse tipo de código que ele fez para pegar a posição
#funciona com matrizes de até 9x9.

#o 10-1 é para que não tenha que ser feita a conversão
#de que uma matriz começa pelo indice 0.
#sendo assim, pode-se referir ao primeiro elemento como
#1 e não como 0.

constroimatriz(m, n, matriz)
print(matriz)

pos1= int(input('Digite a posição do elemento 1: '))
pos2= int(input('Digite a posição do elemento 2: '))

trocaelemento(pos1, pos2, matriz)
print(matriz)
