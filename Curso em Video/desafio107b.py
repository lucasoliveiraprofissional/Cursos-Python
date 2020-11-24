'''Crie um módulo chamado moeda.py que tenha
as funções incorporadas aumentar(), diminuir(),
dobro() e metade()


Faça também um programa que importe esse módulo
e use algumas dessas funções.'''

'''Fiz a versão b pois quis ver como ele fez.'''


'''Ele fez um arquivo teste dentro da pasta ex107
para testar, e acabou usando esse no video de gabarito
'''

from ex107 import moeda

'''Por enquanto, caso desejemos
digitar um valor para p que seja float,
temos que digitar com o padrão americano
. ao inves de ,  vamos ver como solucionar
isso logo, logo.'''

p= float(input('Digite o preço: R$'))

print(f'A metade de {p} é {moeda.metade(p)}')
#se eu quiser, no parentese onde está o primeiro p, posso colocar ,"US$"
#para que a moeda seja em Dolar, porém não vai converter para real.
#ex.: print(f'A metade de {moeda.moeda(p, "US$")}

print(f'O dobro de {p} é {moeda.dobro(p)}')

print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')

print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
