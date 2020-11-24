'''Strings III - Pensando em Strings como Sequencias.
'''

'''Podemos pensar que a palavra pedro é a mesma coisa que o caractere p + e + d + r + o.'''

'''pedro == "p" + "e" + "d" + "r" + "o" '''

'''Só mandar printar que isso será provado novamente:'''

print('pedro')
print("p" + "e" + "d" + "r" + "o")

'''Podemos pensar nessa palavra como uma lista de caracteres também, o que não deixa de ser.'''

lista= ['p', 'e', 'd', 'r', 'o']

print(lista)

'''é uma lista que contem caracteres, que juntos formam uma palavra. '''

'''Como eu tenho uma lista de caracteres, eu posso percorrer cada caracter dessa lista: '''

for char in lista:
    print(char)

#que é o mesmo que fazer:
for char in "pedro":
    print(char)


'''Strings são uma sequencia de caracteres.'''
'''Os elementos podem ser exibidos normalmente como em uma lista.'''

print(lista[0])
#que é o mesmo que fazer:
print("Pedro"[0])

'''Se eu pegar uma string e fizer ela + outra, eu não estou mudando o valor dela, eu estou
redefinindo, concatenando algo a ela, não estou editanto, estou adicionando.'''

#ex.:
lista += 'abc'

'''Não consigo alterar elementos, pois strings tem caracteristicas de tuplas, que são imutáveis.
Elas se comportam como tuplas.'''

#Slices:

palavra= 'Chiclete com banana'
print(palavra[:8])

#ainda ha a possibilidade de usar a função len para pegar o comprimento.
len(palavra)

#consigo colocar comandos de print no meio da minha string:
palavra= 'Chiclete \ncom\n banana'

print(palavra)

len(palavra)

'''Cada \n ele conta como 1 caractere'''
