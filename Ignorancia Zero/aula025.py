'''Introdução a listas'''

lista= [1,2,3,4,5,6,7,8,9]

print(lista[3])
print(lista[0])

#lista dentro de for:
#vai do elemento 0 ao 5

for i in range(6):
    print(lista[i])

#existem indices negativos, a lista será exibida
#de tras pra frente

lista[-1]

#adicionar elementos na lista:

lista += [7]
print(lista)

#adicionar outra lista dentro da existente:

lista += [0, 0, 0]
print(lista)

#somar elementos dentro da lista:

soma= lista[6] + lista[2]
print(soma)

#mudar valores de elementos:
lista[2]= 7.7
print(lista[2])

#lista a partir de variaveis:
a, b, c, d = 1, 2, 3, 4

lista= [a,b,c,d]
print(lista)

#uma lista do fim ate o começo:
lista[::-1]

#podemos atribuir a uma variavel uma sublista ou uma lista já existente
a= lista[::-1]
print(a)

