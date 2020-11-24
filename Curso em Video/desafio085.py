'''Crie um programa onde o usuário
possa digitar sete valores numéricos
e acadastre-os em uma lista única que
mantenha separados os valores pares e
impares. No final, mostre os valores
pares e impares em ordem crescente.
Ele queria que ordenasse a lista dos
pares e a lista dos ímpares, é fácil
também.
'''

'''A ideia foi colocar os numeros pares
no inicio do vetor e os impares no fim, 
por isso o -1 no comando. Porém não deu certo.'''

numeros= list()
temp= list()

for n in range(0, 7):
    temp.append(int(input(f'{n+1}º Número: ')))

for n in numeros:
    if temp[n] % 2 == 0:
        numeros.append(temp[:])

    if temp[n] % 2 == 1:
        numeros.append(temp[:-1])

print(f'\n {numeros}')