'''Fazer um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o último nome separadamente'''

'''De acordo com a aula 09 o len pode ser usado
O len pode ser usado para medir a quantidade de qualquer coisa
Por exemplo, saber a quantidade de sobrenomes que uma pessoa tem:

quant= nome.split() - poderia ter evitado essa variável quant,
mas para ficar mais explícito, estou fazendo ess exemplo assim

(len(quant)-1)
fiz len-1 porque temos que considerar que o primeiro nome da pessoa
não pode ser considerado um sobrenome.
essa linha será exibida no print como a quantidade de sobrenomes que
a pessoa tem.

no desafio 022, fiz o seguinte:

print('A quantidade de caracteres do seu primeiro nome é: {0}\n'.
format(len(nome.split()[0])))

peguei/separei/isolei o nome.split, o indice 0 desse vetor, que nesse caso é o nome
e, num parenteses antes dele, que será feito depois do split,
contei a quantidade de caracteres dentro desse indice 0 do vetor nome.

o que eu tenho que fazer para exibir o sobrenome da pessoa, uma das formas de se fazer
que é a que eu farei:

vou fazer um nome.split
depois contar com o len a quantidade de elementos que tem dentro de nome.split.
Se no total, tiverem 4 elementos dentro de nome.split,
tenho que considerar 04 indo do índice 0 ao 3, porém não
04 como sendo o último índice do vetor, pois o último índice do
vetor é 03.
Sendo assim, para fazer qualquer coisa com o último sobrenome,
tenho que fazer a contagem de todos os elementos de nome.split
e no fim subtrair 01 dessa conta. Aí sim estarei trabalhando
com o último elemento daquele vetor.


len(nome.split()-1) - assim me refiro ao último elemento

nome.split()[(len(nome.split()-1))]
assim eu digo que, após separar o nome, vou trabalhar com o índice que
refere-se ao seu último elemento.

format(nome.split()[(len(nome.split()-1))] - assim ficará o format
(não sei se precisa dentro do [] desse primento parenteses que engloba
o len-1), mas vou testar mesmo assim, pode ser que não precise

print('último=  {}\n'.format(nome.split()[(len(nome.split())-1))]))
'''

nome= str(input('Digite seu nome completo: ')).strip()

print('\nprimeiro: {}'.format(nome.split()[0]))
print('último: {}'.format(nome.split()[(len(nome.split())-1)]))

'''Consegui sozinho!!!, acho que esse foi o mais difícil
Tentei transformar o split em int(nome.split()), mas isso não daria certo
por isso usei o len, que pega a quantidade de algo, já em int'''