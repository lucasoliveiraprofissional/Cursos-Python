'''Listas: métodos pop, index, insert, sort, clear e copy'''
'''Escreva um programa que receba um numero x e devolva o primeiro
indice de uma lista que contem o elemento x. Caso x não esteja na lista,
imprima uma mensagem adequada.'''

a= [1, 2, 3, 4, 5]

x= int(input('Digite o valor de x: '))

'''Caminho das pedras:
achei= False
i= 0
while not achei and i < len(a):
    if a[i] == x:
        print('Indice de {}: {}'.format(x, i))
        #o elemento digitado x está no indice i

    i+= 1

if not achei:
    print('{} não pertence a lista.'.format(x))
'''
#jeito certo:
#retorna a primeira ocorrencia do elemento na lista
print(a.index(x))

