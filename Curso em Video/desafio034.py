''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
Para salarios inferiores ou iguais, o aumento é de 15%.'''

salario= float(input('Digite o seu salário: R$'))

if salario > 1250:
	print('\nSeu salario após o aumento é: R${:.2f}'.format(salario*1.1))
else:
	print('\nSeu salário após o aumento é: R${:.2f}'.format(salario*1.15))