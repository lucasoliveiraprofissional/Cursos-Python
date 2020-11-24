'''Crie um programa que crie uma
matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.
No final, mostre a matriz na tela,
com a formatação correta.'''

matriz= [[], []]
valor= 0

for b in range (0, 3):
    for c in range (0, 3):
        valor= int(input(f'Digite um valor para [{b}, {c}]: '))

        matriz[b][c].append(valor)

for d in range (0, 3):
    for e in range (0, 3):
            print(matriz[d][e])
