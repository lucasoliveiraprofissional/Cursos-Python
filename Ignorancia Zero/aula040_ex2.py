'''Sobre funções, variaveis locais, nonlocal.'''


def f1():
    comeco= 0
    def f2():
        nonlocal comeco
        print(comeco)
        comeco += 1
    return f2

g= f1()

g()
g()
g()
