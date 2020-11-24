'''Faça um programa que calcule a soma entre todos
os números ímpares que são múltiplis de três e que
se encontram no intervalo de 1 até 500'''

a= 0
for impar in range (1, 500):
    if impar % 2 == 1:
        if impar % 3 == 0:
            a+= impar
            print(impar)

print(a)

''' Versão Guanabara:
soma= 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma= soma + c
        
print(' A soma de todos os valores solicitados é {}'.format(soma))

'''