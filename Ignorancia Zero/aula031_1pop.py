'''Listas: métodos pop, index, insert, sort, clear e copy'''
'''Crie uma lista, peça para o usuário escolher um indice da lista,
imprima o elemento da lista neste indice e o remova da lista, 
depois imprima a lista.'''

a= [1, 2, 3, 4, 5]

print(a)

indice= int(input('Digite o indice(de 0 até {}) do elemento a ser removido: '.format(len(a) - 1)))

''' Caminho das pedras:
print('Elemento: '.format(a[indice]))

b= []

for i in tange(len(a)):
    if i != indice:
        #b é uma lista que recebe os elementos excluidos de a
        b.append(a[i])

a= b
'''

#usando o metodo certo pop:
#primeiro printa o elemento removido, depois a lista sem o elemento
print('Elemento: '.format(a.pop(indice)))

print(a)
