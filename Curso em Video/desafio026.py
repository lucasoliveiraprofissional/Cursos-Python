'''Faça um programa que leia uma frase e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição aparece a primeira vez
- Em que posição ela aparece a ultima vez '''



frase= str(input('Digite uma frase: ')).strip()

print('A letra A aparece {} vezes nessa frase.'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.upper().find('A')))
print('A letra A aparece pela última vez na posição {}.'.format(frase.upper().rfind('A')))

#parametros opcionais do r.find, o que eu procuro, o inicio e o fim.
#no caso que eu coloquei em produção, foi só o fim mesmo.
#ultima= frase.upper().rfind('A',0,len(frase))
'''Variáveis que eu usei, porém não precisa:
quantas= frase.upper().count('A')

primeira= frase.upper().find('A')

ultima= frase.upper().rfind('A')
'''

#fui atrás desse rfind na internet