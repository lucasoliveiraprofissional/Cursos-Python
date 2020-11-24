'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.

Ex.: Digite um número: 1834

unidade:4
dezena:3
centena:8
milhar:1

Tentar matematicamente e com string'''

'''Fazendo de acordo com o Guanabara
Ele quis que colocássemos o str antes do input.
Quis fazer assim pois eu acho que a resolução dele será muito melhor'''

'''num= int(input('Informe um número: '))
n= str(num)

print('\nUnidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''

'''Se eu não digitar um valor que tenha 04 dígitos, dá erro. 
Vamos a maneira matematica:'''

num= int(input('Informe um número: '))

u= num // 1 % 10 #pega o numero, divide por 1 e pega o resto da divisao por 10 desse numero
d= num // 10 % 10 #pega o numero, divide por 10(pq a dezena é uma casa a mais que a da unidade) e pega o resto da divisao por 10 desse numero
c= num // 100 % 10 #pega o numero, divide por 100(pq a centena é uma casa a mais que a da dezena) e pega o resto da divisao por 10 desse numero
m= num // 1000 % 10#pega o numero, divide por 1000(pq a o milhar é uma casa a mais que a da centena) e pega o resto da divisao por 10 desse numero

print('\nUnidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))