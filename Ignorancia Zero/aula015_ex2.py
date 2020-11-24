'''Pegar a quantidade de pessoas e fazer cálculos com a idade delas.
Quer mostrar outra funcao de incremento'''
'''está ensinando algo similar ao format'''

cont= 0
n= int(input('Digite o numero de pessoas: '))

while cont < n:
    print('')
    dia = int(input('Digite o dia de nascimento da pessoa {}: '.format(cont+1)))
    mes = int(input('Digite o mes de nascimento da pessoa {}: '.format(cont+1)))
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(cont+1)))
    idade = int(input('Digite a idade a ser completada da pessoa {}: '.format(cont+1)))

    print('A pessoa {} fará {} anos no dia {}/{}/{}'.format(cont+1, idade, dia, mes, ano+idade))

    cont += 1



#print final do jeito que ele está ensinando(funciona também):
#print('A pessoa fará %i anos no dia %i/%i/%i'%(idade, dia, mes, ano+idade))

'''
i ou d= int
f = float
s = strings'''



