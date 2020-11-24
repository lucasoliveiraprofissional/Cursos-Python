"""Escreva uma função recursiva que retorna a soma de n até 0

Peguei pronto, não estou conseguindo mais pensar nessas lógicas que ele passa.
"""
def calculo2(h2):
    if h2 == 0:
        return 0
    return calculo2(h2 - 1) + h2
h = int(input('Digite um numero: '))
print(calculo2(h))
