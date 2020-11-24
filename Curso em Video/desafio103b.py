'''Faça um programa que tenha uma função chamada ficha(),
que receba dois parametros opcionais: o nome de um jogador
e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.'''

'''Fiz a versão b pois não sabia como ele iria fazer para verificar
se é string e se é numero mesmo. Achei que ele fosse fazer dentro
da função.'''

def ficha(jog= '<desconhecido>', gol=0):
        print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


#Programa principal:
n= str(input('Digite o nome do jogador: '))
g= str(input(f'Digite a quantidade de gols do jogador {n}: '))

if g.isnumeric():
        g= int(g)
else:
        g= 0

if n.strip() == '':
        ficha(gol=g)
else:
        ficha(n, g)


ficha(n, g)
