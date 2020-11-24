#manipulando textos
frase= 'Curso em Vídeo Python'
print(frase)

print('só o indice 3 do vetor:')
print(frase[3], '\n')

print('do indice 3 do vetor até o 13º:')
print(frase[3:13], '\n')

print('do inicio do vetor até o 13º')
print(frase[:13], '\n')

print('do 13 até o final:')
print(frase[13:], '\n')

print('do 1 até o 15º:')
print(frase[1:15], '\n')

print('do 1 até o 15º, pulando de 2 em 2 caracteres:')
print(frase[1:15:2], '\n')

print('do 1 até o fim, pulando de 2 em 2 caracteres:')
print(frase[1::2], '\n')

print('não sei o inicio nem o final, pulando de 2 em 2 caracteres:')
print(frase[::2], '\n')

print('Texto longo: (Usar 3 aspas duplas no começo e no fim)')
print("""Em 2017, o ex-assessor do Planalto foi flagrado pela Polícia Federal (PF), 
em uma ação controlada (planejada pela própria PF), saindo de uma 
pizzaria de São Paulo carregando o dinheiro em uma mala que ele 
havia recebido momentos antes do executivo da J&F Ricardo Saud. \n""")

print('contar quantas vezes tem o na frase:')
print(frase.count('o'), '\n')

print('ver o tamanho da frase:')
print(len(frase), '\n')

print('replace, trocando palavras dentro da frase:')
print(frase.replace('Python','Android'), '\n')

print('a palavra Curso está dentro da frase?')
print('Curso' in frase, '\n')

print('ver a posição que Curso está dentro da frase:')
print(frase.find('Curso'), '\n')

print('escrever a frase depois de um split')
print(frase.split(), '\n')

print('escrever um elemento só da lista, depois da frase estar dividida:')
dividido= frase.split()
print(dividido[0], '\n')

print('escrever uma letra só que está dentro de um dos elementos da lista:')
print(dividido[2][3], '\n')