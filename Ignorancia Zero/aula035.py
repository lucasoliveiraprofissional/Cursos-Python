'''Funções II: Argumentos variáveis e pré-definidos(keyword)'''

'''Escreva uma funçã que obtenha a soma de vários números de entrada'''

def soma(*lista): #o * é usado quando não sabemos quantos argumentos terão, é um argumento variável
    soma_num= 0 #porém se uma função precisa de mais de um argumento, o argumento variável
                #tem que ser o último
    for num in lista:
        soma_num += num

    return soma_num

print(soma(1, 2, 3, 4, 5))