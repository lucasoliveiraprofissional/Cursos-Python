'''
Faça um programa que peça o raio de um círculo, calcule e mostre sua área
'''

from math import pi

raio= float(input('Digite o raio do circulo: '))

area= pi*raio*raio

print('A área do círculo é {:.2f}²'.format(area))