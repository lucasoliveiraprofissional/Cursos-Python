'''Faça um programa que leia nome e peso
de várias pessoas, guardando tudo em uma
lista. No final, mostre:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves.'''

'''Fiz a versão b pois minha logica nao funcionou.
Porque também baseado nesse primeiro, iriam vir outros
com logicas parecidas.'''

temp= []
#lista temporaria
princ= []
#lista principal
mai= men= 0.0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

#sem precisar de contador
    if len(princ) == 0:
        mai= menor= temp[1]
    else:
        if mai < temp[1]:
            mai= temp[1]
        if men > temp[1]:
            men= temp[1]

    princ.append(temp[:])
    temp.clear()

    resp= str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp in 'Nn':
        break

#e eu continuo fazendo merda, usando o contador, quando não precisa
#como no caso abaixo, usando o len
print(f'\nAo todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
if p[1] == men:
    print(f'[{p[0]}]', end='')