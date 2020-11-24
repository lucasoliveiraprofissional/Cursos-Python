'''Faça um programa que leia 4 notas, mostre as notas e a média na tela'''

notas= []
media= 0

for i in range(1, 5):
    nota= float(input('Digite a nota {} de 4: '.format(i)))
    notas.append(nota)
    media += nota

print('')
print('As notas digitadas foram: {}'.format(notas))
print('A média é: {}'.format(media/4))
