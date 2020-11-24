'''Faça um programa que tenha uma função
chamada maior(), que receba vários
parâmetros com valores inteiros.

Seu programa tem que analisar todos os
valores e dizer qual deles é o maior.'''

valor= 0

def maior(num):
    mai= 0

    if valor > mai:
        mai= valor

while True:

    valor= int(input('Digite um número: '))
    maior(valor)

    resp= str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O maior valor é: {mai}')