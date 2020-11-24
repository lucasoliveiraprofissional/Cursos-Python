'''Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão.'''

'''Ele fez o decimo pela formula matematica de uma PA.'''

primeiro= int(input('Digite o primeiro termo: '))
razao= int(input('Digite a razao: '))

#formula da PA:
decimo= primeiro + (10 - 1) * razao
#O 10 ali é porque queremos até o décimo termo.

print('')
#esse print é perfumaria minha que sempre coloco.

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c))