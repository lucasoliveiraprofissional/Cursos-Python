'''For loops e listas'''

'''dá para fazer loops com o range assim também:

numeros= [1,2,3,4]
for i in range(len(numeros)):
   print(numeros[i]) 

ou

for i in numeros:
    print(i)

O range é uma sequencia de numeros.

O vetor é uma sequencia de dados, que nesse caso são numeros.

Entao, nesse caso não é preciso usar o range, pois ambos são
sequencia de numeros.

'''

'''Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor
a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0'''

'''Dica: quando há um numero determinado de loops que serão feitos, crie uma variavel
que receberá esse número de loops, para se preciso, alterá-la rapida de facilmente
no inicio do programa onde está a declaração de variáveis.
Nesse caso é a alunos= 10'''

alunos= 10

medias= []

for i in range(1, alunos+1):
    #para receber as 4 notas:
    notas= 0
    for j in range(1, 5):
        notas+= float(input('Digite a nota {} de 4 do aluno {} de {}: '.format(j, i, alunos)))

    notas /= 4

    medias.append(notas)

#para fazer o processamento das notas >= 7
num= 0

for media in medias:
    if media >= 7.0:
        num+= 1

print('O número de alunos com média maior ou igual a 7.0 é: {}'.format(num))
