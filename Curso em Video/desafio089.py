'''Crie um programa que leia nome e duas
notas de vários alunos e guarde tudo em
uma lista composta. No final, mostre
um boletim contendo a média de cada um
e permita que o usuário possa mostrar
as notas de cada aluno individualmente.'''


notas= list()

while True:
    nota= 0


    while nota < 2:
        notas.append(f'Digite a nota {nota+1} do aluno {alunos}: ')
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')