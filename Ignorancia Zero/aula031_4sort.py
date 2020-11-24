'''Organize os elementos de uma lista em ordem crescente'''

a= [5, 3, 1, 2, 4]
aux= a[:]
b= []

print('Lista: {}'.format(a))

'''Caminho das pedras: 
while len(b) != len(a):
    #enquanto o tamanho da lista b for diferente
    #do da lista a, ele continua a adicionar
    #elementos na lista b
    #precisa comparar os elementos, ver se ele é o menor mesmo
    menor= aux[0]
    for ele in aux:
        if ele < menor:
            menor= ele

    #depois de percorrer os elementos, tem que colocar na ordem, removendo o que não tiver em ordem:
    b.append(menor)
    aux.remove(menor)

a= b
'''

#modo correto:
a.sort()
print('Lista: {}'.format(a))