'''Aula020 - Funções - Parte 1'''

'''print()
len()
float()
input()
int()

São funções, e são funções built in
do Python'''

'''Funções podem servir para o seguinte:
por exemplo: queremos printar uma linha
antes de algum menu.

print('-----------------------')
print('         Menu          ')
print('-----------------------')

podemos fazer uma função para isso:

def lin():
   print('-----------------------')
   
Ficaria:
lin()
print('         Menu          ')
lin()

Mas isso ainda assim gastaria muito
do lin(), e não precisa.

Por isso, podemos otimizar, fazendo
passagens por parametros:

def mensagem(msg):
   print('-----------------------')
   print(msg)
   print('-----------------------')
mensagem('SISTEMA DE ALUNOS')

Exemplo mais na pratica:
def titulo(txt):
   print('-' * 30)
   print(txt)
   print('-' * 30)
   
#programa principal
titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')

'''

'''Aula prática: 
Por exemplo, para evitar 
muitas repetições para fazer um
programa simples de soma:

def soma(a, b):
   s= a + b
   print(s)


#Programa Principal:
soma(4, 5)
soma(8, 9)
soma(2, 1)

#Podemos explicitamente dizer
quais parametros estão sendo passados,
ex.:
soma(a=4, b=5)

Ou mudar de ordem, mas precisa
explicitar:

soma(b=4, a=5)

Só não podemos explicitar + ou -
assim:

soma(b=4, 5)

'''

'''Empacotamento de parametros:
No python é possivel fazer por exemplo:

contador(5,3,4,7,1,2), ele vai retornar
6 pois é a quantidade de parametros que
eu passei

contador(5,3,4) retorna 3, mesmo principio

declarar o contador:

def contador(*num):
   print(contador)


contador(2, 1, 7)

Ou seja, o usuário digitará n numeros,
eu não sei quantos, mas todos os que ele digitar,
voce coloca nessa variavel.
'''

''' Empacotamento de parametros com lista:

Por exemplo, onde tenhamos uma rotina que precisa
dobrar os valores dentro de um vetor consequentemente.

def dobra(lst):
   pos= 0
   while pos<len(lst):
        lst[pos] *= 2
        pos += 1
        

valores= [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
   
'''