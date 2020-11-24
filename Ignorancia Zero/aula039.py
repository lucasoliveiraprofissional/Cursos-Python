'''Funções VI: Recursividade'''

'''Função recursiva é uma função que refere-se a ela mesma.'''

#exemplo - caminho das pedras:
'''
def fatorial(n):
    fat= 1
    for i in range(1, n+1):
        fat *= 1
    return fat

print(fatorial(5))
'''
#exemplo com recursividade:

def fatorial(n):
    if n == 1:
        return n
    return fatorial(n-1) * n

print(fatorial(5))

'''Desse modo, garantimos que a função fatorial rodará em loop'''

