#sortear um dos quatro alunos para apagar a lousa
from random import choice

aluno1= input('Digite o nome do 1º aluno: ')
aluno2= input('Digite o nome do 2º aluno: ')
aluno3= input('Digite o nome do 3º aluno: ')
aluno4= input('Digite o nome do 4º aluno: ')
alunos= [aluno1,aluno2,aluno3,aluno4]#lista para alunos

print('O aluno que apagará a lousa é: {}'.format(choice(alunos))) # sorteia e escreve
