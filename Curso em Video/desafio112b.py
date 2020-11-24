'''Dentro do pacote utilidadesCeV que criamos
no desafio111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja
capaz de funcionar como a função input(), mas
com uma validação de dados para aceitar apenas
valores que sejam monetários.'''

'''Não sei como fazer algo do tipo, por isso fiz
a versão b'''

from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p= dado.leiaDinheiro('Digite o preco: R$')
moeda.resumo(p, 35, 22)

'''A função leiaDinheiro foi criada dentro
do init.py do pacote dado.'''