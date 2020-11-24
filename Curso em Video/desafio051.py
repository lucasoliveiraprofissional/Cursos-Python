'''Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão.'''

primeiro= int(input('Digite o primeiro termo: '))
razao= int(input('Digite a razao: '))

print('')

print(primeiro)
primeiro += razao

for pa in range(1, 10):
    print(primeiro)
    primeiro += razao
