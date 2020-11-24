'''Curso Ignorancia zero.
Achei interessante como ele usa a condição verificando comparando
com True e Falseem um caso tão simples
ele está ensinando if e else nessa aula.
O programa é um bar que veirifica se o usuário é da maioridade.'''

idade= int(input('Digite sua idade: '))
resp= idade >= 18

if resp == True:
    print('Você pode beber a vontade!')

if resp == False:
    print('Você só pode beber refrigerante!')

'''ou para o caso verdadeiro do If, pode colocar assim:

if resp:
    print('Você pode beber a vontade!')'''