'''Desenvolva uma lógica que leia o peso e a altura de
uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida
'''

peso= float(input('Digite seu peso, usando . ao invés de ,: '))
altura= float(input('Digite sua altura, usando . ao invés de ,: '))
imc= peso/(altura*altura)

if imc < 18.5:
    print('Voce está abaixo do peso.')
elif 25 > imc >= 18.5:
    print('Voce está no peso ideal.')
elif 30 > imc >= 25:
    print('Voce está com sobrepeso.')
elif 40 > imc >= 30:
    print('Voce está com obesidade.')
else:
    print('Voce está com obesidade mórbida.')
