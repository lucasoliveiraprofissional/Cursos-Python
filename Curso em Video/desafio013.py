#programa que dá aumento ao funcionario, colocando 15% ao seu salario existente
salario= float(input('Digite seu salario: '))

print('Você recebeu um aumento e agora seu salário é de: R${:.2f}'.format(salario*1.15))
#apareceu dízima periódica, deveria no teste que eu fiz ser 15, mas apareceu 14,99999...
#não sei controlar a máscara de exibição do format em Python