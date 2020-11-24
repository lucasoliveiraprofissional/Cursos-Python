'''Crie um programa que leia nome,
ano de nascimento e carteira de
trabalho e cadastre-os(com idade)
em um dicionário se por acaso a
CTPS for diferente de ZERO, o
dicionário também receberá o ano
de contratação e o salário. Calcule
e acrescente, além da idade, com
 quantos anos a pessoa vai se
 aposentar.'''

'''Fiz versão B pois vacilei, 
demorei para praticar python'''

from datetime import datetime

dados= dict()
dados['nome'] = str(input('Nome: '))

'''Será criada uma variavel normal para
ano de nascimento, ela não estará no
dicionário.'''

nasc= int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc

dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
'''0 significa que a pessoa não tem CTPS'''

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano da sua contratação: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

'''A aposentadoria, ele convencionou aqui,
mas não é regra. É igual a data de contra-
tação mais 35 anos. Mas isso retornará um 
número normal. Para sabermos daqui quantos
anos ele vai se aposentar, precisamos pegar
esses dados, ou seja, a data de contratação
mais 35 anos, menos o ano atual.
Isso também não responde o que precisamos.
Por isso precisamos pegar a idade que ele
tem agora e somar a todo esse número obtido.
Aí saberemos com que idade ele aposentará.'''

for k, v in dados.items():
    print(f'{k} tem o valor {v}.')