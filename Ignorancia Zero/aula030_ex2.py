'''Peça uma lista de numeros inteiros para o usuário e imprima a lista sem repetições'''

n= int(input('Digite o numero de elementos da lista: '))

lista= []
aux= []

for i in range(n):
    elemento= int(input('Digite o elemento {} de {}: '.format(i + 1, n)))
    lista.append(elemento)
    aux.append(elemento)
    #a lista auxiliar no começo tem que ser igual a principal
    #pois queremos fazer alterações na aux e não na principal

print(lista)

for ele in aux:
    aparicoes= lista.count(ele)
    #contamos quantas vezes o elemento 0 aparecerá
    #entre a quantidade de elementos que existem
    #no aux
    for i in range(aparicoes-1):
    #como vamos deixar sem repeticoes, tem que
    #ter pelo menos 1 de cada numero que apareceu
    #por isso não vamos fazer um range completo
    #por isso o aparicoes-1
        lista.remove(ele)
    #ou seja, vai remover todos os elementos
    #até a penultima aparicao dele

print(lista)