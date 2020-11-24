'''Crie um programa que simule o
funcionamento de um caixa eletronico.
No inicio pergunte ao usuário qual o
valor que será sacado(numero inteiro)
e o programa vai informar quantas
cédulas de cada valor serão entregues.

OBS.: Considere que o caixa possui
cédulas de R$50, R$20, R$10 e R$1'''

'''Peguei a versão dele pois me confundo
na lógica de divisões e restos. E já é
o último e já está tarde para eu fritar
meus neuronios pensando nisso.
Tentei me basear no desafio023b mas não deu.'''

'''O total é um montante, desse total inicialmente
eu vou tentar tirar de 50 em 50 reais quantas vezes
for possível para que eu esteja apto a tirar de
20 em 20 depois.'''

valor= int(input('Qual valor você quer sacar? R$'))
total= valor
totced= 0
ced= 50

'''A ideia é ir tirando de 50 em 50 do valor total.
Depois sai do loop quando não der mais para tirar de
50 em 50. Cada 50 que é tirado, aumenta 1 para o contador
daquela cedula.'''

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}.')
        if ced == 50:
            #o valor da cedula precisa ser atualizado.
            #depois que tiramos tudo, não vamos mais
            #poder usar cedulas de 50, só de 20.
            #aí começamos a usar de 20 e assim por
            #diante.
            ced= 20
        elif ced == 20:
            ced= 10
        elif ced == 10:
            ced= 1
        totced= 0
        if total == 0:
            break

print('Volte sempre!')

'''Eu não conseguiria nunca fazer isso por minha lógica propria.'''