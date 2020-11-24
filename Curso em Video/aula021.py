'''Aula 021 - Funções - Parte 2'''

'''
Interactive Help
Docstrings
Funcoes com argumentos opcionais
Escopo de variaveis
Retorno dos resultados'''

'''Interactive help
é um built in do Python

Como usar:

Se formos no console do Python
(tipo o IDLE), podemos digitar
help().

Depois de digitarmos esse comando,
podemos perguntar sobre qualquer
função.

Ex.:
print

Ele mostrará os parâmetros esperados com sua
explicação detalhada, parametros opcionais e etc...

p/ sair, basta digitar quit

ou mostrar a ajuda interativa de outra forma:

help(print)

ou de outro modo:

print(input.__doc__)
'''

'''Docstrings:

é uma string de documentação, a help(input) é a
docstring do comando input.

Criando docstring:

def contador(i, f, p):
    c= i
    while c <= f:
        print(f '`{c}', end= '..')
        c += p
    print('Fim!')
    
    
contador(3, 10, 2)


Para que possamos deixar claro nesse código para
que terceiros o compreendam também, usamos as docstrings.

Antes da linha c= i, dentro da função, ou seja, logo depois,
na linha seguinte da def, coloca-se a docstring.

Colocamos 3 aspas duplas e fechamos com 3 também. O Pycharm já 
começa a completar com docstring quando digitamos isso dentro
da função.

Ficaria assim mais ou menos:

(3 aspas) A função tal faz isso xpto
    :parametro i: faz isso
    :parametro f: faz isso
    :parametro p: faz isso
    :return: sem retorno
    
(3 aspas)

Agora quando chamarmos por help(contador)
ele vai mostrar a docstring que digitamos.
'''

'''Parametros opcionais:

Quando eu determino um parametro opcional,
eu o faço indicando com =0 depois dele. Ex.:

def somar(a=0, b=0, c=0):
    s= a+b+c
    print(f'A soma vale (s)')
    
    
somar(3,2,5)
somar(8,4)
somar()

Nesse caso, como a ultima chamada não contém
parâmetros, ele é aceitável, receberá 0 e printará
0.

No help(print) por exemplo, só o 1º parametro é
obrigatório:

print(value, ..., sep='', end='\n', file=sys.stdout, fflush=False)'''

'''Escopo de variáveis:
escopo global(fora do def)

def teste(b):
    a= 8
    b += 4
    c= 2
    
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    
aqui termina o escopo local

escopo global(fora do def)

a= 5
teste(a)
print(f'A fora vale {a}')


no escopo local:
a vai receber 8
b vai receber 9
c vai receber 2

no escopo global:
a vai receber 5
'''

'''Retornando valores:
def somar(a= 0, b=0, c=0):
    s= a+b+c
    return s
    
    
r1= somar(3,2,5)
r2= somar(1,7)
r3= somar(4)

print(f'Meus calculos deram {r1},{r2} e {r3}')

Prática:

(caso o usuário não digite nada, o valor padrão
da função fatorial será 1)

def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f *= c
    return f
    
    
n= int(input('Digite um numero: ))

print (fatorial(n))

ou:

f1= fatorial(5)
f2= fatorial(4)
f3= fatorial()

print(f1, f2, f3)

***********************
Aplicação interessante:
***********************

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
        

num= int(input('Digite um numero: '))

if par(num):
    print('é par!')
else:
    print('é ímpar!')
    
    
'''