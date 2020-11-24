'''listas: função len e método count'''

#pegar o tamanho de uma lista:
#len(lista)

'''Recebendo entradas inteiras do usuário que só devem ser interrompidas com a
entrada do número -1, e recebendo um elemento qualquer, calcular o número
de vezes que esse elemento aparece na sequencia digitada pelo usuario'''

lista= []


num= int(input('Digite um numero da sequencia: '))

while num != -1:
    #append pela primeira vez que o while vai executar:
    lista.append(num)
    #num que repetirá dentro da condição do while:
    num = int(input('Digite um numero da sequencia: '))

elemento= int(input('Digite o elemento a ser procurado: '))

#comentários da versão caminho das pedras:
#temos que dar uma conferida em cada elemento digitado pelo usuário
#cada vez que ele digita, temos que conferir.
#como nao sabemos quantas vezes ele vai digitar, temos que fazer um
#for que a variavel de incremento é o tamanho da lista, e usar esse retorno pro for


'''
Versão caminho das pedras pra depois aprender o mais facil:
cont= 0
for i in range(len(lista)):
    if lista[i] == elemento:
        cont += 1


print('A quantidade de vezes que o elemento foi digitado é: {}'.format(cont))
'''
#versão facil:

print('A quantidade de vezes que o elemento foi digitado é: {}'.format(lista.count(elemento)))

#o retorno do metodo count pode ser atribuido a uma variavel também.