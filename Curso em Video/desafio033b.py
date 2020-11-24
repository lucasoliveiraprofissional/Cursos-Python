'''faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor

Fazendo de acordo com o Guanabara
Quis fazer assim pois eu acho que a resolução dele será muito melhor'''



a= float(input('Digite um número: '))
b= float(input('Digite outro número: '))
c= float(input('Digite o último número: '))

#verificando quem é o menor

menor=a
if b<a and b<c:
	menor= b
if c<a and c<b:
	menor= c

#verificando quem é o maior
maior= a
if b>a and b>c
	maior= b
if c>a and c>b:
	maior=c

print('O maior numero é o: {} e o menor é o: {}'.format(maior,menor)')