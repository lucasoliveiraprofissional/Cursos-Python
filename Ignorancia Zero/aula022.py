'''A função print: formatação'''

'''O depto Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperatura informadas, bem
como a média das temperaturas.'''

num= int(input('Digite o número de temperaturas registradas: '))

soma= maior= menor= float(input('Digite a temperatura 1: '))

#como o usuario ja digitou a primeira, iniciaremos o for
#a partir da segunda.
for i in range(2, num+1):
        temp= float(input('Digite a temperatura {}: '.format(i)))

        if temp > maior:
            maior= temp

        if temp < menor:
            menor= temp

        soma += temp

print('A maior temperatura é: {:.2f}ºC'.format(maior))
print('A menor temperatura é: {:.2f}ºC'.format(menor))
print('A média das temperaturas é: {:.2f}ºC'.format(soma/num))