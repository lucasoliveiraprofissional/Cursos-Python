'''Faça um programa que mostre todos os primos entre 1 e N
sendo N um numero inteiro fornecido pelo usuario.
O programa deverá mostrar também o número de
divisões que ele executou para encontrar os números
primos.
Serão avaliados o funcionamento, o estilo e o número de
testes (divisões) executados.'''

n= int(input('Digite o valor de n: '))
div= 0
for i in range(1, n+1):
    #for para percorrer todas as divisoes possiveis até o proprio numero primo:
    primo= True
    #atraves do for, serão feitas divisoes desnecessarias, para isso tem que
    #ser o while
    j= 2
    while j < i and primo:
        div += 1
        if i % j == 0:
            primo= False

    if primo:
        print(i)
print('Divisoes {}'.format(div))
