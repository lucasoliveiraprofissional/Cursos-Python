'''Faça um programa que verifique se uma letra difitada é
"F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo inválido.
'''

x= input('Digite uma letra: ')

if x == 'M' or x == 'm':
    print('M - Masculino')
elif x == 'F' or x == 'f':
    print('F - Feminino')
else:
    print('Entrada Inválida!')

    