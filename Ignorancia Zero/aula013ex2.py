'''Dado um numero inteiro não-negativo n, determinar n!'''

n= int(input('Digite n: '))

'''
prod= n
cont= n-1
while cont > 1:
    prod = prod*cont
    cont= cont - 1
print(prod)
'''

#outro modo:


prod= 1
cont= 2

while cont <= n:
    prod= prod * cont
    cont= cont + 1
print(prod)

