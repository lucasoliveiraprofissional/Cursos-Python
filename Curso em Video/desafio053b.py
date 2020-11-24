'''Crie um programa que leia uma frase qualquer e diga
se ela é um palindromo, desconsiderando os espaços.'''

'''Eu consegui chegar até uma certa distancia, mas travei
porque não conseguia fazer o for enxergar ao mesmo tempo
a quantidade de elementos de minha string transformada
em lista(só listas tem comprimentos) e ao mesmo tempo
que precisa enxergar como string. Essas manipulações
todas com cópia da lista original para não afetar
o original, não funcionaram direito.'''

'''Resumindo: essa é a resoluçao do Guanabara'''

frase= str(input('Digite uma frase: ')).strip().upper()

palavras= frase.split()
junto= ''.join(palavras)

inverso= ''

for letra in range(len(junto) - 1, -1, -1):
#teste print(junto[letra])
    inverso += junto[letra]

if junto == inverso:
    print('É palindromo')
else:
    print('Não é palindromo')