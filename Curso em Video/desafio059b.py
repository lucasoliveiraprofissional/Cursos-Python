'''Crie um prgrama que leia dois valores
e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação
solicitada em cada caso.'''

'''Fui procurar a versão do Gustavo pois 
sei que vai ficar menor e que estará funcionando
perfeitamente, ocorreram alguns testes com a minha
e eu não gostei totalmente do resultado.'''

from time import sleep

n1= float(input('Primeiro valor: '))
n2= float(input('Segundo valor: '))

opcao= 0

while opcao != 5:

    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    opcao= int(input('Qual é sua opção? '))

    if opcao == 1:
        print('Voce escolheu somar. ')
        print('A soma dos números é: {:.2f}'.format(n1 + n2))
        print('')
    elif opcao == 2:
        print('Voce escolheu multiplicar. ')
        print('O produto dos números é: {:.2f}'.format(n1 * n2))
        print('')
    elif opcao == 3:
        print('Voce escolheu maior.')
        if n1 > n2:
            print('O maior número é: {:.2f}'.format(n1))
        elif n2 < n1:
            print('O maior número é: {:.2f}'.format(n2))
        else:
            print('Os números são iguais.')
        print('')
    elif opcao == 4:
        print('Voce escolheu a opcao novos números: ')
        n1 = n2 = 0
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print('')
    elif opcao == 5:
        print('Fim!')
        sleep(3)
    else:
        print('Opcao inválida! Digite novamente!')
print('Fim!')