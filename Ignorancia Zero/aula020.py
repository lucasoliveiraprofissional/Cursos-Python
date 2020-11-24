'''Fazer um programa que colete 3 notas e calcule em seguida
a mensagem reprovado ou aprovado tem que aparecer se a nota
for menor ou maior igual a 7
se a média for 10, tem que ser aprovado com distincao'''

media= float(input('Digite a primeira nota:'))
media+= float(input('Digite a segunda nota:'))
media+= float(input('Digite a terceira nota:'))

media /= 3

if media == 10:
    print('Aprovado com distinçao')
elif media >= 7:
    print('Aprovado.')
    print('Media {}'.format(media))
else:
    print('Reprovado')
    print('Media {}'.format(media))

#ou do seguinte jeito:
'''
if media >= 7 and media != 10:
    print('Aprovado.')
elif media < 7:
    print('Aprovado.')
    print('Media {}'.format(media))
else:
    print('Aprovado com distincao')
'''