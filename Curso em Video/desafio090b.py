'''Faça um programa que leia nome e média
de um aluno, guardando também a situação
em um dicionário. No final, mostre o
conteúdo da estrutura na tela.'''

'''Fiz versão B pois vacilei, 
demorei para praticar python'''

aluno= dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao']= 'Aprovado'

elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'

else:
    aluno['situacao'] = 'Reprovado'

print('')
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

