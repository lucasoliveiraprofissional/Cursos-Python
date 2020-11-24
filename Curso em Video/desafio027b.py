'''Fazer um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o último nome separadamente'''

'''Fazendo de acordo com o Guanabara
Ele quis que colocássemos o str antes do input.
Quis fazer assim pois eu acho que a resolução dele será muito melhor'''

n= str(input('Digite seu nome completo: ')).strip()
nome= n.split()

print('Seu primeiro nome é: '.format(nome[0]))
print('Seu último nome é: '.format((nome[len(nome)-1])))
