'''baseado na altura e sexo de uma pessoa, calcular o peso ideal
formulas:
homens: (72.7*h) - 58
mulheres: (62.1*h) - 44.7 (h= altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso'''

h= float(input('Informe sua altura: '))
sexo= str(input('Informe seu sexo (M ou F): '))
peso= float(input('Informe seu peso: '))

pesoh= (72.7 * h)-58
pesom= (62.1 * h)-44.7

if sexo == 'M':
    if peso == pesoh:
        print('Voce está dentro do peso.')
    if peso < pesoh:
        print('Voce está abaixo do peso.')
    else:
        print('Voce está acima do peso.')
else:
    if peso == pesom:
        print('Voce está dentro do peso.')
    if peso < pesom:
        print('Voce está abaixo do peso.')
    else:
        print('Voce está acima do peso.')