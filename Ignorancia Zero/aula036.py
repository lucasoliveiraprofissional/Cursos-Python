'''variáveis globais e locais'''

'''Por exemplo:
x= 10

def incrementa(x):
    incremento= 5 #var local
    x += incremento
    print(x)

print(x)
'''

'''x vale 10, porém todas as vezes que eu pedir a funcao incrementa,
o x vai entrar lá, vai pegar um valor de uma variavel local, que é a incremento,
vai somar a si e vai printar já somado esse valor a ele

Se eu porém só pedir um print x, ele vai printar o valor de x comum, o que foi
definido primeiro, o que o x é na verdade, o que ele continua valendo, que é
10'''

'''Para dizermos ao Python que queremos trabalhar com uma variável global, temos que informar
que ela é global: '''

X= 10

def incrementa():
    global X
    incremento= 5 #variavel local
    X += incremento

incrementa()

print(X) #agora o X valerá 15, e só deixará de ter esse valor quando mudarmos ele posteriormente.