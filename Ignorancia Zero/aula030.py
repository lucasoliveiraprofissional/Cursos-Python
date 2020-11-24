'''Listas método reverse e remove'''

'''Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida'''


idades= []
alturas= []

for i in range(1, 6):
    idade= int(input('Digite a idade da pessoa {} de 5: '.format(i)))
    altura= float(input('Digite a altura(m) da pessoa {} de 5: '.format(i)))

    idades.append(idade)
    alturas.append(altura)

''' Caminho das pedras:
#usando slice:
idades_invertida= idades[::-1]
alturas_invertida= alturas[::-1]

for i in range(5):
    print('Idade {}: {}'.format(5 - i, idades_invertida[i]))
    print('Altura {}: {:.2f}'.format(5 - i, alturas_invertida[i]))
'''

'''Caminho das pedras:
#usando range:
for i in range(4, -1, -1):
    print('Idade {}: {}'.format(i + 1, idades[i]))
    print('Altura {}: {}'.format(i + 1, alturas[i]))
'''

#usando reverse (metodo certo):
idades.reverse()
alturas.reverse()

for i in range(5):
    print('Idade {}: {}'.format(5 - i, idades[i]))
    print('Altura {}: {:.2f}'.format(5 - i, alturas[i]))

