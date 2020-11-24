'''Erros e exceções:
ex.: primt(x) - erro sintaxe

    print(x) - exceção(não inicializamos variavel x)

n= int
mas usuario digitou ('oito')
= ValueError - Excelçao tipo variavel,
errada. Esperava inteiro, não caractere.


a= int
b= int

a/b (sendo que a= 8 e b= 0)
= ZeroDivisionError - Divisão por 0 não existe.

r= 2/ '2'
= Type error - s/ divisão de int ou float por caractere.

lst= [3, 6, 4]
print(lst[3])
= IndexError - não existe índice 3 nesse caso.

import uteis (sendo que uteis não existe nesse caso)
= ModuleNotFoundError - módulo não encontrado!
'''

'''
Como tratar exceções no python:

try:
    operação
except:
    falhou
else:
    deu certo
finally:
    certo/falha
    
    
com mais exceções:

try:
    operação
except TypeError:
    falhou
except ValueError:
    falhou
except OSError:
    falhou
else:
    deu certo
finally:
    certo/falha
'''

try:
    a= int(input('Numerador: '))
    a = int(input('Denominador: '))
    r= a / b

except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é: {r:.1f}')

#ao inves de fazer a linha 62, fazemos um dos excepts abaixo
#ou colocamos todos juntos
except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de dado que você'
          'digitou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
    
except KeyboardInterrupt:
    print('O usuário preferiu não digitar os dados.')

'''O tipo de exceção KeyboardInterrupt ocorre quando o
usuário digita CTRL + C ou clica no botão STOP do compilador.'''

'''Ou uma outra opção, o Except genérico também pode ser adicionada: '''

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')