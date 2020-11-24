'''Crie um programa que tenha uma tupla
com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para
cada palavra, quais são suas vogais.'''

palavras= ('abacate', 'ovo', 'maracuja',
           'linguica')

a= e= i= o= u= [0, 0, 0, 0]

for verif in range (0, len(palavras)):
    aux= palavras[verif]

    if aux.count('a'):
        a[verif] += 1
    if aux.count('e'):
        e[verif] += 1
    if aux.count('i'):
        i[verif] += 1
    if aux.count('o'):
        o[verif] += 1
    if aux.count('u'):
        u[verif] += 1

print(a[0]+1)

'''
for verif in aux:
    print(f'Quantidade de letras A da palavra {palavras[verif]}:{a[verif]+1}')
    print(f'Quantidade de letras E da palavra {palavras[verif]}:{e[verif]+1}')
    print(f'Quantidade de letras I da palavra {palavras[verif]}:{i[verif]+1}')
    print(f'Quantidade de letras O da palavra {palavras[verif]}:{o[verif]+1}')
    print(f'Quantidade de letras U da palavra {palavras[verif]}:{u[verif]+1}')
'''