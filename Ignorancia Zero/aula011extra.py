'''Mostrando elif para um caso interessante
3 numeros lidos serão mostrados em ordem decrescente'''

a= int(input('Digite o primeiro numero: '))
b= int(input('Digite o segundo numero: '))
c= int(input('Digite o terceiro numero: '))


'''Jeito errado: 
if a < b:
    if a < c:
        if b < c:
            print(c, b, a)
        else:
            print(b, c, a)
    else:
        print(b, a, c)
'''

#jeito certo:

if a >= b >= c:
    print(a, b, c)
elif a >= c >= b:
    print(a, c, b)
elif b >= a >= c:
    print(b, a, c)
elif b >= c >= a:
    print(b, c, a)
elif c >= a >= b:
    print(c, a, b)
else:
    print(c, b, a)

