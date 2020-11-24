'''Função list, comparação entre listas'''

#list é um tipo de dados, assim com int e float

#list pode receber por exemplo:

'''
Fazer isso no Python console/ Idle
list([1, 2, 3])
print(list)

list('dsalkjdslkjdsa')
print(list)

list(range(1,20))
print(list)
'''

#ex 1
'''No site da megasena está escrito que a chance de um jogador ganhar é de 1 em 50.063.860.
Escreva um programa usando o módulo random e os conceitos utilizados em aula para testar
essa probabilidade.'''

import random

meu= [6, 13, 25, 33, 42, 50]

megasena= list(range(1, 61))

n= int(input('Numero de testes: '))

soma= 0

for i in range(n):
    sorteado= []
    cont= 0

    #enquanto eu não tiver ganhado
    while meu != sorteado:
        #para não ficarmos operando direto sobre a variavel megasena,
        #temos que criar uma variavel que tenha o mesmo conteudo que ela

        mega_sort = megasena.copy()

        sorteado= []
        #sorteado tem que ficar vazio, para que dentro do while
        #outra sequencia seja sorteada até que eu ganhe

        #esse processo tem que ser feito 6x pois a megasena tem 6 numeros
        for j in range(6):
            num_sorteado= random.choice(mega_sort)
            sorteado.append(num_sorteado)
            #remove o numero sorteado para nao repetir
            mega_sort.remove(num_sorteado)

        #se os mesmos numeros nossos forem sorteados, porém não na mesma ordem,
        #vamos precisar que seja colocado na ordem para compará-los depois.
        sorteado.sort()

        cont+= 1

    soma+= cont
    #demonstrara no fim do while

    print('Resultado do teste {}: {} tentativas'.format(i+1, cont))

soma/= n

print('Média dos resultados: {}'.format(soma))