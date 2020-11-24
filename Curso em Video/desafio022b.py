'''criar um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome '''

'''Fazendo de acordo com o Guanabara
Ele quis que colocássemos o str antes do input
e quis que considerássemos a hipótese do usuário
digitar espaços antes e depois de digitar o nome'''

nome= str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem ao todo {} letras'.format(nome.find(' ')))
separa= nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


'''Achei legal que ele já colocou o .strip no começo, eu colocaria no .format
ele colocou de um jeito muito mais fácil a operação para descontar a quantidade de 
espaços em branco que tiver, no -nome.count(' ')

Achei muito inteligente como ele fez pra saber quantas letras tem o primeiro nome,
de modo que quando digitamos um espaço, já acabamos o primeiro nome, ou seja, o primeiro
espaço retornará o índice do vetor que contou até ali, mas para o leigo que não
considera o número zero como início, esse número que retorna é exatamente a quantidade
de letras que o nome tem. Porém essa técnica não considera se o usuário digitar 
espaços antes, já com meu split, que fiz no código, isso é considerado, apesar
de dar mais trabalho.
'''