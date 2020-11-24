'''criar um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome '''

'''Vou tentar fazer o menos possível usando variáveis'''

'''Ele pediu para que começássemos a usar o str
antes do input. Após ver o vídeo da solução do exercício,
essa foi a única alteração que fiz nesse código.'''

nome= str(input('Digite seu nome completo: '))

#maiusculo:
print('\nSeu nome em maiúsculo: {}\n'.format(nome.upper()))
#minusculo:
print('Seu nome em minúsculo: {}\n'.format(nome.lower()))

#sem considerar espaços
#primeiro quero fazer um replace que não salvará a variável, para remover os espaços
#depois disso eu conto

print('A quantidade de letras de seu nome desconsiderando os espaços: {}\n'.format(len(nome.replace(' ',''))))
#o mesmo, porém com o split:
#print('A quantidade de letras de seu nome desconsiderando os espaços, pelo split é: {}\n'.format(len(''.join((nome.split())))))


#a quantidade de letras do primeiro nome
#primeiro eu tenho que fazer um split, pegar o primeiro índice dessa lista, usando o indice da lista
#e depois fazer a conta desse elemento
print('A quantidade de caracteres do seu primeiro nome é: {0}\n'.format(len(nome.split()[0])))

#frase.split()

#CONSEGUI!!! TUDO SOZINHO, SEM PRECISAR USAR O YOUTUBE, SÓ ME BASEEI NA MINHA AULA
#09 QUE EU COMENTEI BEM