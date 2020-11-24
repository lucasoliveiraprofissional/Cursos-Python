'''Refaça o desafio 051, lendo o primeiro termo e a
razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.'''

'''Me baseei no exercicio 051b pois o Guanabara
pegou a formula de uma PA.'''

'''Quis colocar a resolução dele aqui, apensar de
na minha ter funcionado também. A dele ficou
um pouco diferente da minha, mas interessante.'''

'''No meu código eu não precisaria pegar a fórmula
da PA, porém, precisaria fazer igual ao desafio061b,
com a sintaxe exatamente igual.'''

primeiro= int(input('Primeiro termo: '))
razao= int(input('Razão da PA: '))
termo= primeiro
cont= 1

print('')

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo+= razao
    cont += 1
print('Fim')
