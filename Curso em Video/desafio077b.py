'''Crie um programa que tenha uma tupla
com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para
cada palavra, quais são suas vogais.'''

'''Quis fazer a versão dele pois na minha
eu acho que eu estava complicando demais
e se eu fosse tentar fazer o que ele sugere
eu iria complicar ainda mais, fora o nó que
estava dando na minha cabeça para pensar na
lógica.'''

palavras= ('APRENDER',
           'PROGRAMAR',
           'LINGUAGEM',
           'PYTHON',
           'CURSO',
           'GRATIS',
           'ESTUDAR',
           'PRATICAR',
           'TRABALHAR',
           'MERCADO',
           'PROGRAMADOR',
           'FUTURO')

for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

'''Opção para considerar vogais, ainda que
elas tenham acento:
linha 29: in 'aãáâeéêiou' '''

'''Nesse desafio, um passo adiante seria pegar a posição
que cada vogal está, acrescer num acumulador referente
aquela vogal, e depois printar a vogal localizada naquela
posição.

Já no if que verifica se vogal in letra, dá para fazer um
if e um in para cada vogal, mas no exemplo do prof, ele fez
um in considerando todas as vogais de uma vez só.

Não coloco essa possibilidade aqui pois ocuparia muitas linhas
e pela explicação e no momento em que estou escrevendo isso, dá
para entender o que eu quero dizer.'''