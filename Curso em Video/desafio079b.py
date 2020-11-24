'''Crie um programa onde o usuário possa
digitar vários valores numericos e
cadastre-os em uma lista. Caso
o número já exista lá dentro, ele
não será adicionado.
No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.'''

numeros= []

while True:
    n= int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar.')

    r= str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break

numeros.sort()
print(f'Voce digitou os valores: {numeros}')

''' codigo que eu tinha feito:
while True:
    pergunta = ''
    
    n= int()
    
    if cont == 0:
        numeros.append(int(input('Digite um valor: ')))
    else:
        while numeros[cont] in numeros:
            print(f'Valor duplicado! Não vou adicionar...')
            pergunta= input('Quer continuar? [S/N] ').strip().upper()[0]
            if pergunta == 'N':
                break

            if pergunta == 'N':
                break

            else:
                numeros.append(int(input('Digite um valor: ')))
                pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]
                cont += 1

                if pergunta == 'N':
                    break
'''

