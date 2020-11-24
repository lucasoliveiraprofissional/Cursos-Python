'''Lambda:'''

def soma(x, y, z):
    return x+y+z

a= soma
a(1, 2, 3)

f= (lambda x, y, z: x + y + z)
print(f'{f(1, 2, 3)}')

'''O Lambda nesse caso tem a mesma função que a função soma().
Ou seja, ele adere a função que atribuimos a ele.
O lambda precisa de uma variável.'''

'''sintaxe:
variavel = (lambda <argumentos da expressão>: <o que voce quer que retorne>)'''

'''Soma por exemplo não precisa de uma variavel.
Eu posso fazer uma soma(1, 2, 3) a qualquer momento no meu código.'''

'''Lambda fornece funções fáceis e simples que retornam um valor.'''

'''Lambda é chamado também de função anonima, pois ele não tem
nome definido como o soma()'''

'''Podem existir lambdas aninhados.'''