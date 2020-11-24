'''Faça um programa que tenha uma função
chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento)
e mostre a área do terreno.'''

def area(largura, comprimento):
    result= largura * comprimento

    print(f'A área de um terreno {largura:.2f}x{comprimento:.2f} é de {result:.2f}m².')

largura= float(input('LARGURA (m): '))
comprimento= float(input('COMPRIMENTO (m): '))

area(largura,comprimento)