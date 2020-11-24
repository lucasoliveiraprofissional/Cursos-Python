'''Modifique as funções que foram criadas
no desafio107 para que elas aceitem um
parametro a mais, informando se o valor
retornado por eles vai ser ou não formatado
ela função moeda() desenvolvida no desafio108
'''

'''As coisas que ele quis fazer com as funções
ainda estão muito abstratas para que eu faça do 
zero, fiz a versão b por isso.'''

from ex109 import moeda


p= float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True):.2f}')
#o primeiro moeda é o modulo, o segundo moeda é a função

print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
#o primeiro moeda é o modulo, o segundo moeda é a função

print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')

print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')

'''Para evitar o moeda.moeda do exercicio anterior,
ele criou um novo parametro nas funcoes, o Formato,
que recebe um valor boolean.
E agora temos que colocar o parametro para o formato quando
quisermos printar formatado.'''