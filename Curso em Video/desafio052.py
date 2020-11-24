'''Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo.'''

num= int(input('Digite um número: '))
divisoes= 0

'''Pra tirar o peso da consciencia, eu estava
tentado ver se ele era ou não divisivel
apenas atraves de uma variavel booleana, mas
não ia dar certo. O correto é ver quantas vezes
o número é divisível pelo número que passa no for.
Se ele for divisivel por mais de 2 vezes, não é primo.'''
# a condição num % c == 0 estava certa, eu fiz de cabeça.


#vi o video da resolução do exercicio, e coloquei o +1
#depois do num, no último parametro.
for c in range(1, num+1):
    if num % c == 0:
        divisoes+= 1

    if divisoes == 2:
        print('O número é primo.')
    else:
        print('O número não é primo.')