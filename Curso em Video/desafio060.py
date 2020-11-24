'''Faça um programa que leia um número qualquer
e mostre o seu fatorial.'''

num= int(input('Digite um número: '))
c= num

while c > 2:
     #num*= num
     c-= 1
     c= c * (c-1)
     print(c)

#print('Fatorial é {}'.format(num))
