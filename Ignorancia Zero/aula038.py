'''Funções 5: Nomenclatura e descrição'''

'''Evitar dentro de uma função criar uma variável que tenha
o mesmo nome da função'''

'''Funções são alocadas em endereços de memória'''

'''se eu tiver uma função f por exemplo e atribui-la a uma
variável x por exemplo, x vira uma função igual a f'''
#exemplo:

def f(ops):
    num= ops
    print(num)

f(1)

x= f

print(x)

x(2)
f(2)
'''x(2) e f(2) farão a mesma coisa e mostrarão o mesmo resultado.'''

'''Mesmo que depois o f vire variável, o x continua sendo uma função,
como determinamos anteriormente'''

#descrição de funcao:
#exemplo:
#help(print)   escrito no Idle

'''tudo o que vier como resposta é a descrição da função'''

'''Se eu criar uma função e dentro dela colocar comentário de mais de uma linha e depois dar
help(nome da função criada) no Idle, o Python me retornará esse comentário que escrevi.'''

'''Esse comentário criado é a descrição da função, onde está o nome dela, o que ela faz,
recebe, retorna, etc...'''

