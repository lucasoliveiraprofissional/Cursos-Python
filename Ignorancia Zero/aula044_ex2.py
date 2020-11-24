"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos
restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a
sua média, conforme a descrição acima informada (retirar o melhor e o pior salto
e depois calcular a média com as notas restantes). As notas não são informados
ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

Tente colocar a impressão do resultado em um único print
"""

notas = []
soma = 0

nome = input("Atleta: ")

for i in range(7):
    nota = float(input('Nota: '))
    soma += nota
    notas.append(nota)

soma -= min(notas)
soma -= max(notas)

media = soma / (len(notas) - 2)
#menos 2 é pq temos que desconsiderar a menor e a maior nota. Ou somente soma / 5 já valeria.

print(f'\nResultado final:\nAtleta: {nome}\nMelhor nota: {max(notas):.1f}\nPior nota: {min(notas):.1f}\nMédia : {media:.2f}')
