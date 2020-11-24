'''Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será
a base de conversão:

-1 para binário
-2 para octal
-3 para hexadecimal'''

#fazendo junto com o professor, pois não entendi a
#sintaxe que achei na internet

num= int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('-1 para binário')
print('-2 para octal')
print('-3 para hexadecimal')
opc= int(input('Digite sua opção: '))
print('')

'''Vai ficar aqui o comentário, antes da parte de processamento,
pois tem um detalhe.

Se escolhermos binário, antes do número, ele printa 0b,
Se escolhermos octal, antes do número, ele printa 0o,
Se escolhermos hexadecimal, antes do número, ele printa 0x.

Vamos transformar em uma string para podermos fazer os
tratamentos necessários. O [2:] indica que queremos
que ele printe a partir do 3º digito da variavel,
que é onde queremos.'''

if opc == 1:
    print('O número digitado na base binário é {}'.format(bin(num)[2:]))
elif opc == 2:
    print('O número digitado na base octal é {}'.format(oct(num)[2:]))
elif opc == 3:
    num= str(hex(num)[2:]) #aqui eu já transformei pois quis que
                           #sempre que fosse hexadecimal, o numero
                           #viesse em maiusculo.
    print('O número digitado na base hexadecimal é {}'.format(num.upper()))
else:
    print('Opção inválida, digite novamente.')

