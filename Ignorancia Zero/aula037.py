'''Funções IV - Listas e Matrizes'''

'''Listas que são por exemplo modificadas dentro de uma função,
ficarão modificadas definitivamente até quando quisermos
modificá-las mpva,emte depois. ex.:'''
'''Ao que parece, não tem muito isso de global e local com listas'''

def modificalista(a):
    a[0] += 10


a= [1, 2, 3, 4]

modificalista(a)

print(a)