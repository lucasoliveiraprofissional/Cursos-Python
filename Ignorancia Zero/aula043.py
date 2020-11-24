'''Statements Break e Continue'''

'''Break serve dentro de for também.'''

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    for j in range(10):
        if j == 5:
            break
        print(i, j)

'''Nesse caso, o break faz com que o processamento do código
volte pro laço j.'''

'''Mesma coisa, mas em while:'''

i= 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1


'''continue '''

for i in range(10):
    if i == 5:
        continue
    print(i)

'''Nesse caso, ele não printou o 5, pois o continue não prossegue,
o continue nesse caso, faz com que o programa volte pro for, ou seja,
volte para o ultimo procedimento/laço feito.'''

for i in range(5):
    for j in range(5):
        if j == 3:
            continue
        print(i, j)

'''Nesse caso, o continue faz com que o processamento do código
volte pro laço j.'''