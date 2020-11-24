'''Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai
pagar.'''

'''Calcule o valor da prestação mensal, sabendo que ela não 
pode exceder 30% do salário ou então o empréstimo será negado.'''

print('Empréstimo bancário: ')
print('')

valor_casa= float(input('Digite o valor da casa: '))
salario= float(input('Digite seu salario: '))
anos= int(input('Em quantos anos voce vai pagar a casa: '))
print('')

salario_porc= salario * 0.3

prestacao= (valor_casa / anos)/ 12

if prestacao <= salario_porc:
    print('Você pagará mensalmente: R${:.2f}'.format(prestacao))

else:
    print('Voce não poderá pagar essa casa pois o valor '
          'da prestação é maior que a porcentagem aceitável de seu '
          'salário.')
