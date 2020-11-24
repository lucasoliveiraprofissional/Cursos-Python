'''
Dada uma sequencia de numeros inteiros não-nulos
seguida por 0, imprimir seus quadrados.
'''

'''
n = int(input('Digite o numero: '))
while n != 0:
    n = int(input('Digite o numero: '))
    print(n*n)
'''
'''Exercicios de casa: Soma de números positivos inteiros
e sequencia de numeros inteiros ímpares'''

#EXERCÍCIO DE CASA 01:
'''
n = int(input("Digite um número inteiro positivo: "))
x=0
soma=0
if n > 0:
    while x < n:
     soma += (n-x)
     x+=1
    print("A soma dos %d primeiros inteiros positivos é %d." %(n,soma))
else:
    print("Digite apenas números inteiros positivos.")
'''

#EXERCÍCIO DE CASA 02:
'''
n = int(input("Digite um número inteiro positivo: "))
y=0
x=1
if n > 0:
    while y < n:
        print(x)
        y+=1
        x+=2
else:
    print("Digite somente números inteiros positivos.")
'''