'''Faça um programa que leia um nome de usuário e a sua senha e não aceite
a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando
a pedir as informações. '''

def main():
    nome= str(input('Digite seu nome: '))
    senha= str(input(''))

    while tudoMaiusculo(nome) == tudoMaiusculo(senha):
        print('Senha igual ao nome!')
        senha= str(input('Digite novamente: '))


def tudoMaiusculo(string):
    maiusculo= ''

    for char in string:
        if 'a' <= char <= 'z':
            char= chr(ord(char) - (ord('a') - ord('A')))
        maiusculo += char

    return maiusculo

main()