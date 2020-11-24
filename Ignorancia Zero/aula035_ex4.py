"""
Escreva uma função que obtenha o maior número de uma sequência de números

Peguei pronto, pois ia demorar para chegar nessa logica que ele propoe
"""

def maior_num(*nums):

    maior = nums[0]
    for i in range(len(nums)):
        if maior < nums[i]:
             maior = nums [i]

    return maior

