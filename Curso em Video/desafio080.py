'''Crie um programa onde o usuário possa
digitar cinco valores numéricos e cadastre-
os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.'''

'''Fiz do jeito burro, mas vou fazer a versão 080b
pois quero ver como ele fez os inserts e os pops.'''

numeros= []
aux= aux2= int

for cont in range(0, 5):
    numeros.append(int(input('Digite um numero: ')))

    anterior= cont-1

    aux= numeros[cont]

    if aux < numeros[anterior]:
        aux2= numeros[anterior]
        numeros[cont]= aux2
        numeros[anterior]= aux

    aux= aux2= int

print(numeros)