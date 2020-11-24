'''Crie um programa que leia vários números
inteiros. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor
valor lido. O programa deve perguntar ao usuário
se ele quer continuar ou não a digitar valores.'''

'''Eu quis conferir como ele fez.'''

resp= 'S'
soma= quant= media= maior= menor= 0

while resp in 'Ss':
    num= int(input('Digite um número: '))
    soma += num
    quant+= 1

    if quant == 1:
        maior= menor= num
    else:
        if num > maior:
            maior= num
        if num < menor:
            menor= num

    resp= str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    #esse .strip eu acho frescura dele, mas blz.

media= soma / quant

print('Voce digitou {} numero e a media foi {}'.format(quant, media))

print('Msior numero {} menor {}'.format(maior, menor))
