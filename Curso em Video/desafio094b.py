'''Crie um programa que leia nome, sexo
e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No
final, mostre:

A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas
com idade acima da média.'''

'''Fiz versão B pois vacilei, 
demorei para praticar python'''

galera= list()
pessoa= dict()
soma= media= 0
mulheres= list()

'''Como serão várias pessoas, há
necessidade de loop nisso.'''

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        '''Para limpar o registro anterior.'''
        pessoa.clear()
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Digite o sexo corretamente na próxima vez!')

    pessoa['idade']= int(input('Idade: '))
    soma+= pessoa['idade']

    if pessoa['sexo'] in 'F':
        mulheres.append(pessoa['nome'])

    galera.append(pessoa.copy())

    while True:
        resp= str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N.')

    if resp == 'N':
        break

print('')
'''A) quantas pessoas são cadastradas:'''
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')


'''B) media das idades:'''
media= soma / len(galera)
print(f'A média das idades é de {media:.2f} anos.')


'''C) As mulheres cadastradas: '''
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:
        print(f'{p["nome"]} ', end='')


'''D) Lista de pessoas que estão acima da média: '''
print('As pessoas acima da média são: ', end='')
for p in galera:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}')
        print('')
print('Encerrado')

'''O único detalhe é que eu queria calcular a média das idades
no print, sem precisar da variável soma, mas eu não ia acertar 
tão fácil.'''

'''Ele estava com a ideia para mostrar as mulheres, mas não
funcionou:

 For pra cada pessoa em galera:

for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print('')

Eu tive que pegar e adicionar em uma lista as mulheres,
na medida que elas eram cadastradas. Essa foi a única
alteração do código.

'''