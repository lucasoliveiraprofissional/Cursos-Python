'''Código binário e alocação de memória'''

'''
O Python faz esse gerenciamento de memoria explicado abaixo, outras linguagens não.

a= 10
a. bit_lenght()

esse metodo pega a quantidade de bits necessários para representar a como variavel

a= 10
b= a

a ocupará um certo espaço na memória, em certa localidade
b ocupará o mesmo espaço na memória, porém em outra localidade

lista1= [1, 2, 3]
lista2= lista1

ambas as variaveis terão o mesmo tamanho e ocuparao o mesmo local na memoria

se eu fizer lista2[0]= 8000
lista1[0] também valerá 8000 pois estão no mesmo local

isso se aplica a listas dentro de listas

lista de variaveis
l1= [a, b]
l1  é 1, 10
a= 2
l1 continua sendo 1,10

variaveis sao atreladas a valores e não a localidades
listas sao atreladas a localidades
'''