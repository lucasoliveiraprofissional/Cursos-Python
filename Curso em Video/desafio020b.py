#sortear a ordem de apresentação dos trabalhos dos alunos
# VERSÃO ACOMPANHANDO PROF - não quis pegar tudo pronto no Youtube
from random import shuffle

aluno1= input('Digite o nome do 1º aluno: ')
aluno2= input('Digite o nome do 2º aluno: ')
aluno3= input('Digite o nome do 3º aluno: ')
aluno4= input('Digite o nome do 4º aluno: ')
alunos= [aluno1,aluno2,aluno3,aluno4]#lista para alunos
shuffle(alunos)

print('A ordem dos alunos é:')
print(alunos)
