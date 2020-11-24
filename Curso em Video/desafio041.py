'''A confederação nacional de natação precisa de um
programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER'''

ano= int(input('Qual é o ano de seu nascimento? '))

idade= 2019-ano

if idade <= 9:
    print('Voce competirá na categoria MIRIM')
elif 14 >= idade > 9:
    print('Voce competirá na categoria INFANTIL')
elif 19 >= idade > 14:
    print('Voce competirá na categoria JUNIOR')
elif 20 >= idade > 19:
    print('Voce competirá na categoria SENIOR')
else:
    print('Voce competirá na categoria MASTER')
