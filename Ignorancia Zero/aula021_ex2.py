'''Faça um programa que peça um numero e
informe se o numero é inteiro ou decimal.
Se o numero for decimal, arredonde o número'''

num= float(input('Digite um número: '))

if num != int(num):
    #a parte decimal de um numero é o que vem depois da virgula,
    #para isso, usamos uma variavel que recebe o que vem depois da virgula
    decimal= num - int(num)
    #o arredondado é a parte inteira do meu numero
    arredondado= int(num)
    if decimal >= 0.5:
        arredondado += 1
    print('{} é decimal.')
    print('Arredondando: {}'.format(arredondado))
else:
    print('{} é inteiro.')

'''toda essa parte do arredondado feita, com os ifs,
é feita automaticamente se usarmos a função round(variavel numerica)'''