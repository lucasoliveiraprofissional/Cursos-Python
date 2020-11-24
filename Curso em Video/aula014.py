'''Estrutura de repetição while'''

'''for c in range (1, 10):
    print(c)
print('Sim')'''

'''
c= 1

while c < 10:
    print(c)
    c+= 1
print('Fim')'''

#while sem quantidade, só para quando digita 0:
'''
n= 1
while n != 0:
    n= int(input('Digite um valor: '))
print('Fim')
'''

'''Mesma situação, porém contando pares e impares:
par= 0
impar= 0

n= 1
while n != 0:
    n= int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par+= 1
        else:
            impar+= 1
        
print('Pares {}, Impares {}'.format(par, impar))
'''