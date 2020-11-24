'''Faça um programa que mostre a tabuada de
vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for
negativo.'''

while True:
    num= int(input('Digite um valor(numero negativo para parar): '))
    print('')

    if num < 0:
        break

    for multiplicador in range(0, 11):
        print(f'{num} X {multiplicador} = {num * multiplicador}')

    print('')

