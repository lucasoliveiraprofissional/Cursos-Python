def aumentar(preco= 0, taxa= 0, formato= False):
    """
    Calcula o aumento de m determinado preco,
    retornando o resultado com ou sem formatacao.

    :param preco: o preco que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saida formatada ou não?
    :return: o valor reajustado com ou sem formato.
    """

    res= preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


'''Essa variavel res fez todo o sentido
agora, uma vez que anteriormente ela não
seria necessária. Seria necessário apenas
o return.
Porém agora com o parametro format,
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


def resumo(preco= 0, taxaa= 10, taxar= 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de reducao: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)


'''Agora criamos a função resumo. No fim dela,
ela chama a função moeda, dobro, etc...
Ou seja, creio ser aqui nesse curso a primeira 
vez que uma função chama a outra.
O\t é uma tabulação

O interessante é que ele passou o taxaa e taxar
para outra funcao. Sendo que o valor de taxaa e
taxar está somente na funcao resumo.
'''
