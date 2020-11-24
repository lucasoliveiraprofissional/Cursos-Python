'''Exemplo: peso de provas.'''

def soma(*nums):
    soma_num= 0

    for num in nums:
        soma_num += num

    return soma_num

def media(p1, p2, p3, peso1, peso2, peso3):
    return (p1*peso1 + p2*peso2 + p3*peso3)/soma(peso1, peso2, peso3)

print(media(5, 5, 5, 1, 1, 1))

'''Ou definindo os valores dos argumentos:

def media(p1, p2, p3, peso1= 1, peso2= 1, peso3= 1):
    return (p1*peso1 + p2*peso2 + p3*peso3)/soma(peso1, peso2, peso3)

print(media(5, 5, 5)) aí omite o valor dos pesos, pois eles apareceram anteriormente'''
'''Os argumentos pré-definidos também tem que ficar no fim de uma função'''