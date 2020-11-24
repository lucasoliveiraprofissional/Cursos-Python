'''Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal
e condição de pagamento:

-à vista dinheiro/cheque: 10% de desconto
-à vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros'''

preco= float(input('Qual o preço do produto? '))

print(('\nEscolha as seguintes formas de pagamento:\n'
                 '[1]Para à vista em Dinheiro/Cheque\n'
                 '[2]Para à vista no Cartão\n'
                 '[3]Para 2x no Cartão\n'
                 '[0]Para mais vezes no Cartão'))
meio= int(input('\nDigite sua opção: '))

if meio == 1:
    print('O produto terá desconto de 10%. '
          'O produto custará: R${:.2f}'.format(preco*0.9))
elif meio == 2:
    print('O produto terá desconto de 5%. '
          'O produto custará: R${:.2f}'.format(preco*0.95))
elif meio == 3:
    print('O produto não terá desconto. '
          'O produto custará: R${:.2f}'.format(preco))
elif meio == 0:
    vezes= int(input('Em quantas vezes você quer pagar? '))

    #laço para não deixar o usuário escolher à vista
    #ou em até 2x nesse menu, pois essa opção já foi
    #informada anteriormente.

    while vezes <= 2:
        print('\nJá existe uma opção para isso, ela deveria '
              'Ter sido selecionada antes. Agora você '
              'terá que pagar em mais vezes.')
        vezes = int(input('Em quantas vezes você quer pagar? '))

    #aqui volta ao processamento normal:

    if vezes >= 3:
        print('\nO produto terá 20% de acréscimo em seu preço. '
              'O produto custará: R${:.2f}'.format(preco*1.2))

else:
    print('Opção inválida!')

