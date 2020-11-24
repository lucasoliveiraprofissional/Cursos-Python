def metade(preco= 0):
    res= preco / 2
    return res


def dobro(preco= 0):
    res= preco * 2
    return res


def aumentar(preco= 0, taxa= 0):
    res= preco + (preco * taxa/100)
    return res

def diminuir(preco= 0, taxa= 0):
    res = preco - (preco * taxa/100)
    return res


'''
um moeda é o nome da funcao, o outro é do parametro
se eu não informar qual a moeda, o padrão vai ser 
real. Se eu não informar o preço, vai ser 0
'''
def moeda(preco= 0, moeda= 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')
#retornara uma string formatada
