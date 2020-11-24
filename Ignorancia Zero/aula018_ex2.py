'''Dados n e n sequencias de numeros inteiros não-nulos,
cada qual seguida por um 0,
calcular a soma dos números pares de cada sequencia
A sequencia acaba quando o usuário digitar 0'''

n= int(input('Digite o numero de sequencias: '))

print('')
for i in range(n):
    #para ficar mais claro ao usuário, vamos imprimir
    #o numero da sequencia
    print('Sequencia: {}'.format(i+1))
    #precisamos verificar cada numero da sequencia,
    #pois um deles pode atender a nossa condição
    num= int('Digite um numero da sequencia: ')
    #soma dos numeros pares de cada sequencia
    #para cada sequencia eu tenho que zerar essa variavel
    soma= 0
    while num != 0:
        #para verificar se o numero é par antes de somar:
        if num % 2 == 0:
            soma += num
        #para ver se o usuário vai ou não digitar 0 e
        #sair do programa:
        num = int('Digite um numero da sequencia: ')

    print('A soma da sequencia {} é: {}'.format(i+1,soma))
    print('')
    