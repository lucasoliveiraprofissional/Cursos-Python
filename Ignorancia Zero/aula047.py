'''Strings - IV: Padrão ASCII, Comparações e Operador In'''

'''American Standard Code for Information Interchange'''

'''For para mostrar a tabela ASCII:'''

for i in range(256):
    print(f'{i} {chr(i)}')

#o Python vai alem dos 255, até 800 por exemplo.

'''chr requer um valor e retorna o caractere correspondente
na tabela ASCII.'''

'''%c tem a mesma função que o chr'''

print(ord('c'))

'''ord pega o numero na tabela ASCII referente aquele caractere.'''

'''No IDLE é possível fazer comparações de strings, ex:'''

'''"a" == "c"'''

'''ord('a') == ord('c') '''

'''Ex1.: '''

'''Faça duas funções: Uma que coloque um string em maiusculo e outra
que coloque uma str em minusculo.'''

def main():
    string= 'CHiCleTe'

    print(tudoMinusculo(string))
    print(tudoMaiusculo(string))


def tudoMinusculo(string):
    minusculo= ''

    for char in string:
        if 'A' <= char <= 'Z':
            char= chr(ord(char) + (ord('a') - ord('A')))
        minusculo += char

    return minusculo

def tudoMaiusculo(string):
    maiusculo= ''

    for char in string:
        if 'a' <= char <= 'z':
            char= chr(ord(char) - (ord('a') - ord('A')))
        maiusculo += char

    return maiusculo

main()

