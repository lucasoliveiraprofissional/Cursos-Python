'''Desenvolva um programa que leia o nome, idade
e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.'''

maior= 0
media= 0
idademulher= 0
nomevelho= ''

for c in range(0, 4):
    nome= str(input('Digite seu nome: '))
    idade= int(input('Digite sua idade: '))
    sexo= str(input('Digite seu sexo M ou F: ')).upper()
    print('')

    media+= idade

    'Para a variavel maior ter um primeiro parametro'
    'Para pegar só de homens'

    '''Eu estava fazendo: 
        if sexo == 'M':
        if idade > maior: Mas o correto é o que ficou
        Vi no vídeo do Guanabara. Se bem que do jeito
        que eu fiz funcionou. Ele resumiu um if colocando
        and e fez outro if para a maior idade de homem
        logo abaixo.'''

    if sexo == 'M' and c == 0:
            maior= idade
            nomevelho= nome

    if sexo == 'M' and idade > maior:
        maior= idade
        nomevelho = nome

    '''Na idade mulher, eu posso usar and
    para comparar parametros diferentes,
    eu usei um if para cada tipo de parametro.
    E depois fiz de acordo com o Gustavo.'''

    if sexo == 'F' and idade < 20:
            idademulher+= 1

print('\nA média de idade do grupo é: {}'.format(media / 4))
print('O nome do homem mais velho é: {}'.format(nomevelho))
print('{} Mulheres tem menos de 20 anos.'.format(idademulher))

