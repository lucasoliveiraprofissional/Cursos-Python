'''Crie um programa que tenha uma tupla
única com nomes de produtos e seus respectivos
preços, na sequencia.

No final, mostre uma listagem de preços, organizando
os dados de forma tabular.'''

listagem= ('Lápis', 1.75,
           'Borracha', 2,
           'Caderno', 15.90,
           'Estojo', 25,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.32,
           'Canetas', 22.30,
           'Livro', 34.90)

'''Ele quis fazer por printar par, depois impares,
uma vez que todo impar é texto e todo par número. '''

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]}:.<30', end='')
    else:
        print(f'{listagem[pos]}:>7.2f')
'''
produtos= (input('Digite o produto: '), float(input('Digite seu preço: R$')),
           input('Digite o produto: '), float(input('Digite seu preço: R$')),
           input('Digite o produto: '), float(input('Digite seu preço: R$')),
           input('Digite o produto: '), float(input('Digite seu preço: R$')),
           input('Digite o produto: '), float(input('Digite seu preço: R$')),
           input('Digite o produto: '), float(input('Digite seu preço: R$')))

for n in produtos:
    print(f'{n} .*20 R${n+1}')
'''