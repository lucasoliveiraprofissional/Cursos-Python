'''Crie um pacote chamado utilidadesCeV
que tenha dois módulos internos chamados
moeda e dado.

Transfira todas as funções utilizadas
nos desafios 107, 108 e 109 para o primeiro
pacote e mantenha tudo funcionando.
'''

'''As coisas que ele quis fazer com as funções
ainda estão muito abstratas para que eu faça do 
zero, fiz a versão b por isso.'''


from ex111.utilidades import moeda

p= float(input('Digite o preço: R$'))
moeda.resumo(p)


'''Dentro do pacote ex111, clicamos com o
botão direito e criamos um pacote: utilidaedscev.'''

'''Dentro do pacote utilidadescev, clicamos com o
botão direito e criamos um pacote: moeda'''

'''Dentro do pacote utilidadescev, clicamos com o
botão direito e criamos um pacote: dado'''

'''Mudei o desafio111 de lugar, pois a chance de dar
problema agora é maior. Então coloquei ele na pasta
ex111 ao invés da Scripts'''

'''Mudou o import, não funcionou de jeito nenhum,
nem do jeito antigo que eu estava fazendo.'''