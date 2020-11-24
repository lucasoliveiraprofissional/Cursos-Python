'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.

Ex.: Digite um número: 1834

unidade:4
dezena:3
centena:8
milhar:1

Tentar matematicamente e com string'''

'''Ele pediu para que começássemos a usar o str
antes do input. Após ver o vídeo da solução do exercício22,
essa foi a única alteração que fiz nesse código.'''


#matematicamente primeiro:
#numero= int(input('Digite um número: '))
#aux = (numero / 1000)
#aux = aux * 1000
#print(aux)


'''
print('\nunidade: {}\n')
print('dezena: {}\n')
print('centena: {}\n'.format((((numero) // 1000)* 1000)))
print('milhar: {}\n'.format(numero // 1000))
'''
#via string por último:

numero= str(input('Digite um numero: '))

print('\nunidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))

