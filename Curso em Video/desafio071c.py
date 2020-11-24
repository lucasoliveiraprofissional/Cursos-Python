'''Desafio071, a abordagem mais matemática que eu procurava.
Porém sem o while, mas blz, já é algo.'''

print("=="*16)
print("           BANCO CEV")
print("=="*16)
valor = int(input("Qual valor você quer sacar? R$ "))
cedulas = valor//50
resto = valor%50
if cedulas > 0:
    print("Total de {} cédulas de R$50".format(cedulas))
cedulas = resto//20
resto %= 20
if cedulas > 0:
    print("Total de {} cédulas de R$20".format(cedulas))
cedulas = resto//10
resto %= 10
if cedulas > 0:
    print("Total de {} cédulas de R$10".format(cedulas))
cedulas = resto//1
if cedulas > 0:
    print("Total de {} cédulas de R$1".format(cedulas))
print("=="*16)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")﻿