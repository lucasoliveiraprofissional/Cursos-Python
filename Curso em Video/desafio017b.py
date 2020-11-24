# VERSÃO ACOMPANHANDO PROF - SEM PRECISAR IMPORTAR. Hipotenusa é a raiz quadrada da soma dos quadrados dos catetos

co= float(input('Digite o comprimento do cateto oposto: '))
ca= float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa= (pow((pow(ca,2) + pow(co,2)),1/2))

print('A hipotenusa é: {:.2f}'.format(hipotenusa))