'''Desenvolva um programa que leia a idade
e sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostre:

- Quantas pessoas tem mais de 18 anos.
- Quantos homens foram cadastrados.
- Quantas mulheres têm menos de 20 anos.'''

'''Parecido com o desafio056, peguei muitas
partes dele. Peguei a pergunta do desafio068b.'''

maior= 0
idademulher= 0
homens= 0
continuar= ' '

while continuar != 'N':
    idade= int(input('Digite sua idade: '))
    sexo= str(input('Digite seu sexo M ou F: ')).strip().upper()[0]
    print('')

    if sexo == 'M':
        homens += 1

    if idade > 18:
        maior += 1

    if sexo == 'F' and idade < 20:
            idademulher += 1

    continuar= str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('')
    if continuar == 'N':
        break

print(f'\nPessoas na maioridade: {maior}')
print(f'Quantidade de homens: {homens}')
print(f'{idademulher} Mulheres tem menos de 20 anos.')
