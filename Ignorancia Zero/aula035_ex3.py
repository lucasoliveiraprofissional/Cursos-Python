"""
Escreva uma função que obtenha a multiplicação de vários números de entrada

Peguei pronto, pois ia demorar para chegar nessa logica que ele propoe
"""


def mult(*nums):
    prod = 1
    for num in nums:
        prod *= num

    return prod

print(mult(1,2,3,4,5,6,7,8,9,10))