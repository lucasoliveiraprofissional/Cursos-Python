'''Melhore o desafio 061, perguntando
para o usuário se ele quer mostrar
mais alguns termos. O programa encerra
quando ele disser que quer mostrar
0 termos.'''

'''Quis colocar a resolução dele aqui, apensar de
na minha ter funcionado também. A dele ficou
um pouco diferente da minha, mas interessante.'''

primeiro= int(input('Primeiro termo: '))
razao= int(input('Razão da PA: '))
termo= primeiro
cont= 1
total= 0
mais= 10

print('')

while mais != 0:
    total+= mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa\n')
    mais = int(input('\nVoce quer ver mais quantos termos? '))

print('Fim!')
print('A PA foi finalizada com {} termos mostrados.'.format(total))