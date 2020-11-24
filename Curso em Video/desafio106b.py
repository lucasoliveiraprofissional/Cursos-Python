'''Faça um mini-sistema que utilize o Interactive
Help do Python. O usuário vai digitar o comando
e o manual vai aparecer.
Quando o usuário digitar a palavra FIM, o programa
se encerrará.'''

'''Fiz versão b pois é muito complexo.'''

from time import sleep

c= ('\033[m',               # 0 - sem cores
    '\033[0;30;41mm',       # 1 - vermelho
    '\033[0;30;42mm',       # 2 - verde
    '\033[0;30;43mm',       # 3 - amarelo
    '\033[0;30;44mm',       # 4 - azul
    '\033[0;30;45mm',       # 5 - roxo
    '\033[7;30mm'           # 6 - branco
    );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor= 0):
    tam= len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

#Programa principal:
comando= ''

while True:
    titulo('SISTEMA DE AJUDA PYHELP', 1)
    comando= str(input('Função ou biblioteca? '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    titulo('Até logo!')

