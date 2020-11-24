'''Faça um programa que tenha uma função
chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento)
e mostre a área do terreno.'''

'''Fiz a versão b só para ver como ele ia solucionar mesmo'''

def area(larg, comp):
    a= larg * comp
    print(f'A área de um terreno de'
          f'{l:.2f} de largura e {c:.2f}'
          f'de comprimento é {a:.2f}m².')


#Programa Principal:
l= float(input('LARGURA (m): '))
c= float(input('COMPRIMENTO (m): '))

area(l, c)