'''Interrompendo repetições while'''

cont= 1
'''Com condição a ser atendida em certo ponto:

while cont <=10:
    print(cont, ' ', end='')
    cont+= 1
print('Acabou')
'''

''' Condição atendida sempre, loop infinito:
while True:
    print(cont, ' ', end='')
    cont+= 1
print('Acabou')'''

'''While true é parado pelo Break'''


'''Desafio 064 melhorado/do jeito certo:'''

n = s = 0
while True:
    n= int(input('Digite um número: '))
    if n == 999:
        break
    s+= n
#print('A soma vale {}'.format(s))
#F String:   muito mais ágil:
print(f'a soma vale {s}')

#outro exemplo:
'''
nome= 'Jose'
idade= 33

print(f'O {nome} tem {idade} anos.')
'''
