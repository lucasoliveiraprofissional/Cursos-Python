'''Adapte o código do desafio107, criando
uma função adicional chamada moeda() que
consiga mostrar os valores como um valor
monetário formatado.
'''

'''Fiz a versão b pois a complexidade
dos códigos e chamadas ficou muito alta para
que eu conseguisse fazer sozinho.'''

'''Devido ao objetivo do 108 ser diferente,
ele criou outa pasta nomeada ex108, pois
o moeda do exercicio 108 é diferente
do do 107, aí não daria para usar
um mesmo arquivo para objetivos diferentes,
iria ter que ficar trocando o codigo sempre.'''

from ex108 import moeda

'''Por enquanto, caso desejemos
digitar um valor para p que seja float,
temos que digitar com o padrão americano
. ao inves de ,  vamos ver como solucionar
isso logo, logo.'''

p= float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p)):.2f}')
#se eu quiser, no parentese onde está o primeiro p, posso colocar ,"US$"
#para que a moeda seja em Dolar, porém não vai converter para real.
#ex.: print(f'A metade de {moeda.moeda(p, "US$")}
#o primeiro moeda é o modulo, o segundo moeda é a função

print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
#o primeiro moeda é o modulo, o segundo moeda é a função

print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')

print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')

