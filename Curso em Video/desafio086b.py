'''Crie um programa que crie uma
matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.
No final, mostre a matriz na tela,
com a formatação correta.'''

'''Fiz a versão b pois quis ver o que
na dele não estava igual ao meu, pois
o meu segundo meu raciocinio está certo,
porém não funciona.'''

matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]= int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0 ,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

'''Para que a matriz não fique desalinhada se digitarmos
números muito grandes e número muito pequenos, houve a 
perfumaria, de centralizar no print como iria aparecer
o dado.'''

