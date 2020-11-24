'''Refaça o desafio 035 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado.

Consegui fazer, porém estou seguindo nesse o modo do Prof fazer
pois tem sintaxe mais enxuta

O título do desafio 035 já está no desafio 042

-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end= '')
    # o print daqui de cima será completado com o resultado
    # do tipo de triangulo, presente nos prints abaixo.

    # condição do tipo de triangulo:
    # o Python permite esse tipo de comparação, muito boa!!!
    if r1 == r2 == r3:
        print('Equilátero.')

        '''No Python é possível printar algo e depois em outro
        print continuar o que foi printado anteriormente,
        na mesma linha. Esse foi o exemplo ali acima, depois de
        triangulo. Precisa indicar que no fim da linha não terá
        nada, não terá Enter.
        Depois onde quiser continuar o print, é só dar o comando
        print'''

        '''Em comparações de diferenças, temos que fazer com que o último seja
        comparado com todos os demais, não só com o penúltimo. Pois se fizéssemos
        r1 != r2 != r3 somente, se r1= 4, r2= 3 e r3= 4, ele atenderia a essa
        condição. Por isso temos que fazer a comparação do r3 com o r1 para
        fazer a nossa comparação efetiva mesmo.'''

    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('Os segmentos acima não podem formar um triângulo.')




