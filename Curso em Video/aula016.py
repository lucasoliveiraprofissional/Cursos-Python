'''Mundo 3 - Tuplas'''

'''No Pyhton, temos 3 tipos de variáveis compostas:
- tuplas
- listas
- dicionários'''

'''String é uma variável composta.'''

'''For pode ser usado para tuplas também'''

'''Tuplas são IMUTÁVEIS!!!'''

'''Enquanto o programa estiver em execução, não é
possível mudar uma tupla.'''

'''Tupla () ou sem parenteses    Lista []'''

lanche= ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(lanche)

'''Print perfumaria: '''

for comida in lanche:
    print(f'{comida}')

print(len(lanche))

for cont in range(0, len(lanche)):
    print(cont)

for cont in range(0, len(lanche)):
    print(lanche[cont])

#mostrar tanto o dado quanto a posição:

for pos, comida in enumerate(lanche):
    print(f'{comida} posicao {pos}')
    
#mostrar em ordem alfabetica:
print(sorted(lanche))

#juntar tuplas
a= (2, 5, 4)
b= (5, 8, 1, 2)

c= a + b

print(c)

#pode contar elementos dentro de uma tupla
print(c.count(5))

#podemos mostrar a posicao de determinado elemento:
print(c.index(8))

#tuplas podem receber tipos de dados distintos:

pessoa= ('Gustavo', 39, 'M', 99.88)
print(pessoa)

'''Tuplas não podem ser mudadas, mas podem ser apagadas.'''
del(pessoa)
