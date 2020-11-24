def leiaDinheiro(msg):
    valido= False

    while not valido:
        #já transforma todas as , do dinheiro em . na entrada
        entrada= str(input(msg)).replace(',','.').strip()

        #tratar quando a entrada é vazia ou espaço:
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preco inválido!\033[m')
        else:
            valido= True
            return float(entrada)

'''podemos colocar o leiaint do ex 104 aqui também.'''

def leiaInt(msg):
    ok= False
    valor= 0
    while True:
        n= str(input(msg))

        if n.isnumeric():
            valor= int(n)
            ok= True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor