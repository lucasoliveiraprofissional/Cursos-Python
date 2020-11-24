'''Listas (Parte 1)'''

'''Listas são por [] e são mutáveis'''

'''lista.append adiciona um elemento no fim da lista'''

'''inserir elemento (no caso do exemplo é no começo da lista)
em qualquer local da lista.

lista.insert(local, novo elemento)'''

'''Maneiras de excluir um elemento da lista.
Nesse caso, o elemento 3

del lista[3]
lista.pop(3)
lista.remove('valor que quer remover')
lista.pop() remove o ultimo elemento da lista.

Após o comando de remoção, o Python elimina o valor,
elimina o espaço d memoria que ficou livre
e refaz os indices'''

'''lista.pop() remove o ultimo elemento da lista.'''

'''dá para usar o operador in nas listas.
if algo in lista:
'''

'''Criar listas a partir de range:
valores= list(range(4, 11))

A lista valores então fica assim
valores= [4, 5, 6, 7, 8, 9, 10]'''

'''Se tivermos uma lista desorganizada,
podemos organizar com o método sort
valores.sort()'''

'''Se quisermos a ordem reversa dos valores,
podemos fazer valores.sort(reverse=True)'''

'''tamanho da lista:
len(valores)'''

'''Parte pratica: '''
'''
num= [2, 5, 9, 1]
num[2]= 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
#num.pop()
num.pop(2)
num.insert(2, 2)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
'''
'''O remove procura do inicio da lista até o fim
a primeira incidencia do numero que eu passo no
parametro para o comando remove.'''

'''Uma lista vazia pode começar por lista= [] ou lista= list()'''

valores= []
'''
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posicao {c} valor {v}')
'''

'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} valor {v}')
'''

a= [2, 3, 4, 7]
b= a
#b[2]= 8

print(f' A: {a}')
print(f' B: {b}')

'''Deste modo nós igualamos as variaveis, tudo o que for feito em
um será alterado no outro.'''

'''O correto se desejar fazer uma copia de uma lista em outra,
um receber todos os itens do outro, aí sim fazemos o certo.
(Similar a fatiamento de strings)'''

b= a[:]
b[2]= 8

print(f' A: {a}')
print(f' B: {b}')

'''
Só como anotação, caso seja util:
for c, v in enumerate(numeros):
    print(f'Na posição {c} encontrei o valor {v}!')
'''