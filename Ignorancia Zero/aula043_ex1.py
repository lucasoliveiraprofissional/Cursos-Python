'''Escreva uma função que produza a soma dos primeiros n
números de uma lista com tamanho m'''

def criaLista():
    lista= []

    m= int(input('Digite o tamanho da lista: '))

    for i in range(m):
        ele= float(input(f'Digite o elemento {i+1} de {m}'))
        lista.append(ele)

    return lista


def main():
    l1= criaLista()

    n= int(input('Digite o número de elementos que se deseja somar: '))

    soma= 0
    for i in range(len(l1)):
        if i == n:
            break
        soma += l1[i]

    print(f'A soma é: {soma}')


main()



'''Nesse exercicio por exemplo, se o n for maior que o tamanho da lista l1, vai dar
problema de indexagem, pois não tem como adicionar algo no indice 7 sendo que a lista
tem 06 indices somente por exemplo. Por isso, temos que dar um break, para que
quando venhamos no loop atingir o tamanho de nossa lista, nós paramos. Para fazer isso, usamos
o if i == n'''