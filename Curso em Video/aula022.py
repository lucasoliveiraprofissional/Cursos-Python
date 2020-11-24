'''Começa a modularização:

Surgiu no início da década de 60

Sistemas ficando cada vez maiores

Foco: dividir um programa grande

Foco: aumentar a legibilidade

Foco: facilitar a manutenção

'''

'''
Ao invés de fazer várias funções dentro do programa, modulariza-se:

def fatorial(n):
	f= 1
	for c in range(1, n+1):
		f *= c
	return f


def dobro(n):
	return n*2


def triplo(n):
	return n*3


num= int(input(‘Digite um valor’))
fat= fatorial(num)
print(f’O fatorial de {num} é {fat}’)
print(f‘O dobro de {num} é {dobro(num)}’)
'''

'''
Se fizermos um arquivo uteis.py
com essas funções ali acima, podemos 
importar ele e chamar ele para um outro
arquivo, o principal que queremos executar

Porém tanto o arquivo principal quanto o uteis
tem que estar no mesmo diretorio

Se fizermos por exemplo:

from uteis import dobro, fatorial.

Se por exemplo a biblioteca uteis tiver mais de
um dobro, o dobro que será importado será o último.

Nesses casos, o ideal é fazer um import de uteis

e depois quando precisarmos dela, fazer uteis.fatorial
no meio do código.

'''

'''Vantagens de se ter uma modularização:

-Organização do código
-Facilidade na manutenção
-Ocultação de código detalhado
-Reutilização em outros projetos

'''

'''
Pacotes:

Quando por exemplo tivermos módulos, o úteis.py

Dentro do uteis tenho várias funções.

Se os módulos ficarem grandes demais? 
Ele fica muito sobrecarregado.

Para evitar isso, podemos juntar módulos e sparar por assuntos
em PACOTES.

Aí teremos as mesmas funções, mas um pacote uteis.

Dentro do Pacote uteis, eu posso ter funções só para
tratamento ed números, outra para strings por exemplo
essas separações estarão dentro de módulos.

aí podemos fazer da seguinte forma:
from uteis import datas

ou seja, dentro do pacote uteis, precisarei
do datas.

Para criar um pacote, tem que ir na pasta raiz
que voce está usando para colocar seus projetos.
No meu caso, seria na Scripts.

Então clicar com o botão direito e clicar em Python
Package em New.

E então dentro do pacote uteis, fazer o mesmo procedi
mento para criar os pacotes datas, numeros, strings.

ai no começo do programa principal, se quisermos usar
a função fatorial por exemplo, que está dentro do pacote
números.

Fazemos:
from uteis import numeros

aí no meio do código, quando quisermos usar, fazemos:

numeros.fatorial.



'''

