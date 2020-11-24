def metade(preco):
    res= preco / 2
    return res


def dobro(preco):
    res= preco * 2
    return res


def aumentar(preco, taxa):
    res= preco + (preco * taxa/100)
    return res

def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


'''Meu moeda antigo, antes de ver a versão b do exercicio 107:
def metade(valor):
    return valor / 2


def dobro(valor):
    return valor * 2


def aumentar(valor):
    return valor * 1.1


def diminuir(valor):
    return valor * 0.87

'''