#fazer um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
#que cada litro de tinta pita uma área de 2m²

base= float(input('Digite a largura de sua parede: '))
altura= float(input('Digite a altura de sua parede: '))

result= float(base*altura)
#printar em m²

tinta= float(result/2)

print('Você precisará de {:.2f}l de tinta para pintar a parede que tem {:.2f}m².'.format(tinta,result))
