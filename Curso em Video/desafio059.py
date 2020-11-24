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


opcao= 0

while opcao != 5:
    num1= float(input('Digite o primeiro valor: '))
    num2= float(input('Digite o segundo valor: '))
    print('')

    opcao= int(input('Digite as opções:\n'
          '\n'
          '[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos números\n'
          '[5] sair do programa\n'
          'Digite sua opção: '))

    print('')
    while opcao == 1:
        print('Voce escolheu somar. ')
        print('A soma dos números é: {:.2f}'.format(num1 + num2))
        print('')
        opcao = int(input('Digite as opções:\n'
                          '\n'
                          '[1] somar\n'
                          '[2] multiplicar\n'
                          '[3] maior\n'
                          '[4] novos números\n'
                          '[5] sair do programa\n'
                          'Digite sua opção: '))

    while opcao == 2:
        print('Voce escolheu multiplicar. ')
        print('O produto dos números é: {:.2f}'.format(num1 * num2))
        print('')
        opcao = int(input('Digite as opções:\n'
                          '\n'
                          '[1] somar\n'
                          '[2] multiplicar\n'
                          '[3] maior\n'
                          '[4] novos números\n'
                          '[5] sair do programa\n'
                          'Digite sua opção: '))

    while opcao == 3:
        print('Voce escolheu maior.')
        if num1 > num2:
            print('O maior número é: {:.2f}'.format(num1))
        elif num2 < num1:
            print('O maior número é: {:.2f}'.format(num2))
        else:
            print('Os números são iguais.')
        print('')
        opcao = int(input('Digite as opções:\n'
                          '\n'
                          '[1] somar\n'
                          '[2] multiplicar\n'
                          '[3] maior\n'
                          '[4] novos números\n'
                          '[5] sair do programa\n'
                          'Digite sua opção: '))

    while opcao == 4:
        print('Voce escolheu a opcao novos números: ')
        num1 = num2 = 0
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
        print('')
        opcao = int(input('Digite as opções:\n'
                          '\n'
                          '[1] somar\n'
                          '[2] multiplicar\n'
                          '[3] maior\n'
                          '[4] novos números\n'
                          '[5] sair do programa\n'
                          'Digite sua opção: '))

print('Voce saiu do programa.')

