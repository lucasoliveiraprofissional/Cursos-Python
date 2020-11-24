'''Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para
cada turma.
As turmas não podem ter mais de 40 alunos.'''

turmas= int(input('Digite a quantidade de turmas: '))

soma= 0

for i in range(1, turmas+1):
    qtde= int(input('Digite o número de alunos da turma {}: '.format(i)))

    while qtde > 40 or qtde < 0:
        print('Número de alunos inválido! Digite novamente.')
        qtde = int(input('Digite o número de alunos da turma {}: '.format(i)))
    soma += qtde

print('A média é de {:.2f} alunos por turma.'.format(soma/turmas))

