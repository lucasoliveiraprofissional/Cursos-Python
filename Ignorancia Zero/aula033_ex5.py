'''
Faça um programa com uma função chamada somaImposto.

A função possui dois parametros formais:
    1- taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem
    2- custo, que é o custo de um item antes do imposto.

a função "altera" o valor de custo para incluir o imposto sobre vendas.

Peguei pronto, pois ia demorar para chegar nessa logica que ele propoe
'''

def dilma(custo, taxaImposto):
    return custo + ((custo / 100) * taxaImposto)


valor = float(input("Digite o custo: "))
taxa = float(input("Digite a taxa de imposto: "))

print("Valor total: %.2f" % dilma(valor, taxa))﻿