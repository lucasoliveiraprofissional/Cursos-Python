# VERSÃO ACOMPANHANDO PROF - não quis pegar tudo pronto no Youtube, não quis pensar em radianos e etc
# ele vai informar o seno, cosseno e tangente de um ângulo
#a biblioteca math dá o resultado em radianos. Teremos que converter para graus

from math import sin, cos, tan, radians
#importando somente os métodos que vamos usar, do seno, cosseno e o conversor para radianos
#primeiro temos que converter de radianos para angulos antes de realizar os calculos

angulo= float(input('Digite o ângulo que você deseja: '))

seno= sin(radians(angulo))
cosseno= cos(radians(angulo))
tangente= tan(radians(angulo))

print('O seno é: {:.2f}'.format(seno))
print('O cosseno é: {:.2f}'.format(cosseno))
print('A tangente é: {:.2f}'.format(tangente))

