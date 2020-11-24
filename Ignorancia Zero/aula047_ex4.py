'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
a.  "Telefonou para a vítima?"
b.  "Esteve no local do crime?"
c.  "Mora perto da vítima?"
d.  "Devia para a vítima?"
e.  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''

global suspeito, a, b, c, d, e

def main():

    a= input('a. Telefonou para a vítima? [s/n]: ')
    while tudoMaiusculo(a) != 'S' or tudoMaiusculo(a) != 'N':
            a= ('Resposta inválida! Digite novamente [s/n]: ')
    pergunta(a)

    b = input('a. Esteve no local do crime? [s/n]: ')
    while tudoMaiusculo(b) != 'S' or tudoMaiusculo(b) != 'N':
            b= ('Resposta inválida! Digite novamente [s/n]: ')
    pergunta(b)

    c = input('a. Mora perto da vítima? [s/n]: ')
    while tudoMaiusculo(c) != 'S' or tudoMaiusculo(c) != 'N':
            c= ('Resposta inválida! Digite novamente [s/n]: ')
    pergunta(c)

    d = input('a. Devia para a vítima? [s/n]: ')
    while tudoMaiusculo(d) != 'S' or tudoMaiusculo(d) != 'N':
            d= ('Resposta inválida! Digite novamente [s/n]: ')
    pergunta(d)

    e = input('a. Já trabalhou com a vítima? [s/n]: ')
    while tudoMaiusculo(e) != 'S' or tudoMaiusculo(e) != 'N':
            e= ('Resposta inválida! Digite novamente [s/n]: ')
    pergunta(e)

    juiz()


def juiz():
    global suspeito

    if suspeito <= 1:
        print('Inocente')
    elif suspeito == 2:
        print('Suspeita')
    elif 4 >= suspeito <= 3:
        print('Cúmplice')
    else:
        print('Assassino')



def pergunta(string):
    global suspeito

    if tudoMaiusculo(string) == 'S':
        suspeito += 1
    else:
        suspeito += 0

    return suspeito

def tudoMaiusculo(string):
    maiusculo= ''

    for char in string:
        if 'a' <= char <= 'z':
            char= chr(ord(char) - (ord('a') - ord('A')))
        maiusculo += char

    return maiusculo

main()