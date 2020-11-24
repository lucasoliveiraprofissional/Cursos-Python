'''Estruturas de repetição III: Ciclo for e range'''

'''Exemplo:
n= 10

for cont in range(n):
    print(cont)
    
funciona perfeitamente
'''

'''um range do 2 ao 6 por exemplo:
range(2,6)
'''

'''um range incrementando não só de 1 em 1:
range(2, 12, 2)
'''

'''range decrescente:
range(10, 0, -2)
'''

'''Fazendo n! usando o for loop'''

n= int(input('Digite o numero: '))
fatorial= 1

#o fator é uma variavel qualquer criada só para uso dentro do for
#só para ser o lugar que receberá a incre ou decrementação
for fator in range(2, n+1):
    fatorial *= fator



#ou fazer o mesmo código, mas de trás para frente:
#for fator in range(n, 1, -1)
#    fatorial *= fator

print('{}! é igual a: {}'.format(n, fatorial))