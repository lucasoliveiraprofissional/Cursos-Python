n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está em maiúsculas? ', n.isupper())
print('Está em minúsculas ', n.islower())
print('Está capitalizada? ', n.istitle())

# nesse código, o n é um objeto, todo objeto tem caracteristicas
# e realiza funcionalidades. (nesse exemplo, atributos e métodos)
# nesse caso estamos vendo os métodos, todos esses is fazem parte dos
# objetos tipo string