def aumentar(preco= 0, taxa= 0, formato= False):
    res= preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


'''Essa variavel res fez todo o sentido
agora, uma vez que anteriormente ela não
seria necessária. Seria necessário apenas
o return.
Porém agora com o parametro formato,
podemos ver a condicao, se a resposta
vai vir formatada pela função moeda ou não.'''


def diminuir(preco= 0, taxa= 0, formato= False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco= 0, formato= False):
    res= preco * 2
    return res if formato is False else moeda(res)


def metade(preco= 0, formato= False):
    res= preco / 2
    return res if formato is False else moeda(res)


'''
um moeda é o nome da funcao, o outro é do parametro
se eun não informar qual a moeda, o padrão vai ser 
real. Se eu não informar o preço, vai ser 0
'''
def moeda(preco= 0, moeda= 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')
#retornara uma string formatada


'''Podemos fazer a condicional do return da seguinte
maneira também:
res if not formato else moeda(res)'''


'''Obs.: Eu consertei a ordem das funções,
deixei igual ao do Guanabara.'''
