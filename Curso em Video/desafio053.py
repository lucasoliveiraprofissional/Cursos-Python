'''Crie um programa que leia uma frase qualquer e diga
se ela é um palindromo, desconsiderando os espaços.'''

'''
frase= input('Digite uma frase: ')
print('')
#print(frase)

#print('Splitado: {}'.format(frase.split()))

frase= frase.split()
#print('Joinado: {}'.format(''.join(frase)))
copia= frase.copy() #copia aqui ainda é lista, não é string
print(copia,'Lista')

frase= ''.join(frase)
#print('Tamanho da frase: {}'.format(len(frase)))

print(frase, 'Frase ')

copia= ''.join(copia)

copia= list(copia)

#o mais longe que eu consegui chegar sozinho, mas não queria precisar
#de for,

'''

'''Eu consegui chegar até uma certa distancia, mas travei
porque não conseguia fazer o for enxergar ao mesmo tempo
a quantidade de elementos de minha string transformada
em lista(só listas tem comprimentos) e ao mesmo tempo
que precisa enxergar como string. Essas manipulações
todas com cópia da lista original para não afetar
o original, não funcionaram direito.'''

'''Resumindo: tive que ver o do Guanabara'''


'''Do jeito mais facil:

string = raw_input()
stringSemEspacos = string.replace(' ', '')
stringTodaMinuscula = stringSemEspacos.lower()
stringInvertida = stringTodaMinuscula[::-1]
if stringInvertida == stringTodaMinuscula:
    print "SIM"
else:
    print "NAO"'''


'''Depois de ver o que o Guanabara fez, eu tente novamente,
porém continuo reaproveitando variáveis: '''

''' Não deu certo reaproveitando variáveis.
frase= input('Digite uma frase: ')
print('')
#print(frase)

#print('Splitado: {}'.format(frase.split()))

frase= frase.split()
#print('Joinado: {}'.format(''.join(frase)))

frase= ''.join(frase)
#print('Tamanho da frase: {}'.format(len(frase)))

copia= ''

for c in (len(frase) -1, -1, -1):
    copia += frase[c]

print(copia)'''