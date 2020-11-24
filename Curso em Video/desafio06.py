numero= int(input('Digite um número: '))

print('O dobro do número digitado é: {}\nO triplo do número digitado é: {}\n'
      'A raiz quadrada do número digitado é: {}\n'.format(numero*2,numero*3,pow(numero,1/2)))

#não quis fazer variáveis para isso para testar a maleabilidade do format
#para num futuro de otimizações não precise ocupar espaço na memória usando variáveis