'''Escreva um programa em que dado a posição i e um número qualquer x,
deve-se inserir esse elemento numa lista na posição determinada'''

'''Exemplo:
lista= [1, 2, 3, 4]
Digite a posição: 2
Digite o elemento: 8000
lista= [1, 2, 8000, 3, 4]'''

a= [1, 2, 3, 4]

print('Lista= ', a)

pos= int(input('Digite a posição: '))
ele= int(input('Digite o elemento: '))


'''Caminho das pedras: 
#cria uma lista auxiliar
b= []

#percorrer todos os indices da lista a:
for i in range(len(a)):
    if i == pos:
        b.append(ele)
    #se o indice for diferente da posição
    #adiciona o elemento da lista a que esteja
    #nessa posição

    b.append(a[i])

a= b
print('Lista= ', a)
'''

#jeito certo:
a.insert(pos,ele)
print('Lista= ', a)