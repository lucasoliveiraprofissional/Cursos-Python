'''Melhore o desafio 061, perguntando
para o usuário se ele quer mostrar
mais alguns termos. O programa encerra
quando ele disser que quer mostrar
0 termos.'''

'''Eu não achei a necessidade de colocar
o while dentro do outro porque sempre ele
vai mostrar 10 termos inicialmente, não
há necessidade de colocar um while dentro
de um comportamento constante.'''


primeiro= int(input('Primeiro termo: '))
razao= int(input('Razão da PA: '))
termo= primeiro
cont= 1

print('')

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo+= razao
    cont += 1
print('Fim\n')


resposta= int(input('Voce quer ver mais quantos termos? '))

while resposta != 0:
    respostatot= resposta
    respostatot += cont

    #resposta total é a soma de mais quantos termos o usuario
    #quer ver, junto a última quantidade de termos que o cont
    #printou e acumulou, que até então é 10
    #enquanto o cont, que até então é 10 não chegar a esse
    #valor de resposta total, ele continuará a fazer os
    #cálculos dentro do while.

    while cont <= (respostatot-1):
        #respostatot menos 1 é porque o contador é 10
        #sendo assim ele contará desde o 0 do 10 até
        #o número desejado, printando assim 1 termo
        #a mais do que o desejado.
        #Ou eu faria o cont+1 dentro desse while,
        #ou eu diminuiria o respostatot em -1 para
        #enquadrar-se no desejado.

        '''Agora eu observei na resolução deste
        exercicio, que eu vou colocar um desafio
        062b. No começo do código ele coloca o 
        cont recebendo 1 e não zero. Por isso podemos
        fazer o que eu disse ali em cima e colocar
        o cont recebendo + 1 novamente.'''

        print('{} → '.format(termo), end= '')
        termo+= razao
        cont += 1

    print('Fim')
    resposta = int(input('\nVoce quer ver mais quantos termos? '))
