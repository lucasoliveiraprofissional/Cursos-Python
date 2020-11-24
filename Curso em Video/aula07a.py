# curiosidades: dá para formatar a saída do print
nome = input('Qual é seu nome? ')

print('Prazer em te conhecer {:20}!'.format(nome))
# ele vai printar o nome e depois do nome, até dar 20 caracteres,
# vai preencher com espaço

print('Prazer em te conhecer {:<20}!'.format(nome))
# faz o mesmo, mas alinhando o nome de acordo com os últimos 20 caracteres,
# o nome ficará na direita

print('Prazer em te conhecer {:<20}!'.format(nome))
# faz o mesmo, mas alinhando o nome de acordo com os primeiros 20 caracteres,
# o nome ficará na esquerda

print('Prazer em te conhecer {:^20}!'.format(nome))
# faz o mesmo, mas alinhando o nome de acordo com os 20 caracteres,
# o nome ficará no centro

print('Prazer em te conhecer {:=^20}!'.format(nome))
# faz o mesmo, mas alinhando o nome de acordo com os 20 caracteres,
# o nome ficará no centro e aos lados será preenchido com =

 