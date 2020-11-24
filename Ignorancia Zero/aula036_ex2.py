'''Exercicio para simular o uso de variavel global'''

'''
Bancário. Escreva um programa que registre o caixa de um banco. O programa
começa perguntando se o usuário quer criar uma conta ou fechar o programa. Se
ele escolher fechar o programa escreve uma mensagem de agradecimento e fecha,
caso contrário ele vai pedir que usuário selecione um número com 6 dígitos
e, então, se o número não existir no registro do banco, ele irá pedir um valor
de depósito. Depois o banco perguntara se deseja ver o saldo do banco, se sim
ele deverá imprimir o balanço geral do banco, senão ele entrará em loop.
'''

contas = []
depositos = []
saldo = 0

'''Variáveis globais tem que ficar fora do main, no 'script geral' do programa'''

def main():

    opcao = bool(int(input('Deseja ver o saldo do banco?(1 - Sim | 0 - Não): ')))
    while opcao:
        criaConta()
        VerSaldo()
        opcao = bool(int(input('Deseja ver o saldo do banco?(1 - Sim | 0 - Não): ')))

def criaConta():
    #dá para declarar mais de um global, na mesma linha, tudo de uma vez
    global contas, depositos, saldo
    num_conta= int(input('Digite um numero de conta: '))

    #while para dizer se a conta já existe ou não
    while num_conta in contas:
        print('Conta já existente. Digite novamente.')
        num_conta = int(input('Digite um numero de conta: '))

    contas.append(num_conta)

    deposito= float(input('Digite o valor do seu primeiro depósito: '))
    #só pra validar que foi feito um deposito de algum valor:
    while deposito <= 0:
        print('')
        print('Valor de depósito inválido!')
        deposito = float(input('Digite o valor do seu primeiro depósito: '))

    depositos.append(deposito)
    saldo += deposito

def VerSaldo():
    global saldo
    opcao= bool(int(input('Deseja ver o saldo do banco?(1 - Sim | 0 - Não): ')))
    if opcao:
        print('O saldo do banco é: R$ []'.format(saldo))

main()