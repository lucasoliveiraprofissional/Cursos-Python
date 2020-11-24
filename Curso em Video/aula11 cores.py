'''Trabalhando com cores no terminal

depois da \ contrabarra
colocar um código, que é o que funciona em cores para ANSI, é o 033
antes do m vem o nome da cor de acordo com esse código.

O primeiro paramentro é o código do comportamento(style), normal, sublinhado, etc...
depois ;
o código da cor do texto(text)
depois o código da cor de fundo, background(back)

ex.:
\033[0;33;44m

os parametro são opcionais

códigos para estilo:
0 nada
1 bold
4 underline
7 inverter as cores do fundo e da letra

cor do texto:
30
até
37

cor do fundo:
40
até
47

testes'''

#letra vermelha
print('\033[31mOlá, Mundo!')

#letra vermelha fundo amarelo
print('\033[31;43mOlá, Mundo!')

#letra vermelha fundo amarelo negrito
print('\033[1;31;43mOlá, Mundo!')

#delimitar a linha do background
print('\033[31;43mOlá, Mundo!\033[m')

#pesquisar módulo colorize (cores em hexadecimal)

#colocar cores em determinados pontos do texto somente:
a= 3
b= 5
print('Os valores são \033[32m{}\033[m e \033[31m{}'.format(a,b))

#podemos colocar o código de cor no format:
nome= 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}'.format('\033[m', nome,'\033[m'))