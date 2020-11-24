'''Refaça o desafio 051, lendo o primeiro termo e a
razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.'''

'''Me baseei no exercicio 051b pois o Guanabara
pegou a formula de uma PA.'''

'''No meu código eu não precisaria pegar a fórmula
da PA, porém, precisaria fazer igual ao desafio061b,
com a sintaxe exatamente igual.'''

primeiro= int(input('Digite o primeiro termo: '))
razao= int(input('Digite a razao: '))

#formula da PA:
decimo= primeiro + (10 - 1) * razao
#O 10 ali é porque queremos até o décimo termo.

#print(decimo)
#fiz só pra saber como ficaria o décimo

termocorrente= primeiro

print('')
#esse print é perfumaria minha que sempre coloco.

while termocorrente <= decimo:
    print(termocorrente)
    termocorrente += razao
