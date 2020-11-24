#ler numero real qualquer e mostrar sua porção inteira, sem virgula

from math import trunc

numero= float(input('Digite um número qualquer com ponto: '))
truncado= float(trunc(numero))

print('O numero {} tem a parte inteira {:.0f}'.format(numero, truncado))

