'''Faça um programa que leia o sexo de uma
pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente
até ter um valor correto.'''

sexo = str(input('Digite o sexo da pessoa: ')).upper()

while sexo not in 'MmFf':
    sexo = str(input('Digite corretamente o sexo da pessoa: ')).upper()[0]
print('Fim')

'''Essa sintaxe tem que ser desse jeito. Não funcionou de outro modo,
o [0] não precisa.'''