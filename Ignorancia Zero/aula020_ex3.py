'''Fa�a um pograma que calcule as raizes de uma equacao do segundo grau
na forma ax2 + bx + c. O programa dever� pedir os valores de a, b e c
e fazer as consistencias, informando ao usu�rio nas seguintes situa��es

a. se o usu�rio informar o valor de A igual a zero, a equa��o n�o �
do segundo grau e o programa n�o deve fazer pedir os demais valores,
sendo encerrado;

b. Se o delta calculado for negativo, a equacao n�o possui raizes reais,
Informe ao usu�rio e encerre o programa;

c. Se o delta calculado for igual a zero a equacao possui apenas uma raiz
real; informe a ao usuario;

d. se o delta for positivo, a equacao possui duas raizes reais; informe-as
ao usuario;

delta= b**2 - 4*a*c
raiz= (-b + ou - (delta**(1/2)))/(2*a)
'''

#n�o tive paciencia para fazer esse, peguei um codigo pronto

a = float (input("Informe o valor de A: "))
if a == 0 :
    print "A equa��o n�o � do segundo grau."
else:
    b = float (input("Informe o valor de B: "))
    c = float (input("Informe o valor de C: "))
    delta = (b**2) - (4 * a * c)
    x1 =(((-1)*(b))+(delta**0.5))/(2*a)
    x2 = ((-1*b) - (delta**0.5))/ (2*a)
    if delta < 0:
        print "A equa��o n�o possuir ra�zes reais."
    if delta == 0:
        print "A equa��o possuir apenas uma raiz real que � %f"%(x1)
    if delta > 0:
        print "A equa��o possuir duas ra�zes reais que � %f e %f" %(x1, x2)?