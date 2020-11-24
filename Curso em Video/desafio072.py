'''Crie um programa que tenha uma tupla
totalmente preenchida com uma contagem
por extenso, de zero até vinte.
Seu programa deverá ler um número no teclado
(entre 0 e 20) e mostrá-lo por extenso.'''

extenso= ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num= int(input('Digite o número: '))
    if num > 20 or num < 0:
        print('Opção errada!')
        num = int(input('Digite o número: '))
    else:
        break

print(f'Voce digitou o número {extenso[num]}')

''''''