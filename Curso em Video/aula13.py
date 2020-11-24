'''Estrutura de repetição for'''

for c in range(0, 6):
    print(c)
print('FIM')

for c in range(6, 0, -1):
    print(c)
print('FIM')

for c in range(0, 7, 2):
    print(c)
print('FIM')


n= int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i= int(input('Início: '))
f= int(input('Fim: '))
p= int(input('Passo: '))

s= 0
for c in range(i, f+1, p):
    print(c)

