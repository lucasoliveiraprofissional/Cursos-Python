'''Adicione ao módulo moeda.py criado
nos desafios anteriores, uma função chamada
resumo(), que mostre na tela algumas informações
geradas pelas funções que já temos no módulo
criado até aqui.'''

'''As coisas que ele quis fazer com as funções
ainda estão muito abstratas para que eu faça do 
zero, fiz a versão b por isso.'''

from ex110 import moeda

p= float(input('Digite o preço: R$'))
moeda.resumo(p)

'''Ou se quisermos, podemos passar o
parametro de aumento e redução no
moeda.resumo. Basta fazermos assim:

moeda.resumo(p, 20, 12)'''