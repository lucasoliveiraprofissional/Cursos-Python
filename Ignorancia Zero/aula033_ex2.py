'''2 Função que retorna uma expressão

Faça um programa, com uma função que necessite de três arqumentos,
e que forneça a soma desses três arqumentos.'''

def soma(num1, num2, num3):
    soma_num= num1 + num2 + num3

    return soma_num

'''A função dá um retorno do que é processado dentro dela.
O que é processado dentro dela utiliza os argumentos que são
passados a função.
As variáveis definidas dentro da função são locais e geram um resultado
que irá como retorno a chamada da função.'''

print(soma(1,2,3))

'''Ou:

def soma(num1, num2, num3):
    
    return soma_num
    
print(soma(1,2,3))    
'''