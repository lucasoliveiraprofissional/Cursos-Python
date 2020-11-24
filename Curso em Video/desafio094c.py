'''O problema com  mulheres.append(pessoa['nome'])
KeyError: 'nome'

Me fez recorrer a isso, tive que pegar um que
aparentemente funciona.'''


media = 0
dados = {}
lista = []
meninas = []
while True:
    dados['nome']= str(input('Nome:')).strip().capitalize()
    dados['idade']= int(input('Idade:'))
    media += dados['idade']
    dados['genero']= str(input('genero M/F:')).strip().upper()[0]
    while dados['genero'] not in 'MF':
        dados['genero']=str(input('ERRO. digite corretamente [M/F]')).upper().strip()[0]
    if dados['genero'] in 'F':
        meninas.append(dados['nome'])
    lista.append(dados.copy())
    resp = str(input('deseja continuar s/n:')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('ERRO. deseja continuar [S/N]:')).strip().upper()[0]
    if resp in 'N':
        break

print('='*60)
print(f'A) Total de pessoas cadastradas: {len(lista)}')
print(f'B) A média de idade é de {media / len(lista):.2f} Anos')
if len(meninas) !=0:
    print(f'C) As mulheres são:',end=' ')
    for x in meninas:
        print(x)
else:
    print('Não temos garotas cadastradas.')
print(f'D) Lista das pessoas acima da média:')
for x,y in enumerate(lista):
    if lista[x]["idade"] > media / len(lista):
        print(f' -> nome: {lista[x]["nome"]} idade: {lista[x]["idade"]} genero: {lista[x]["genero"]}')
    else:
        print('Não a pessoas acima da média cadastrada. ')
print('<- ENCERRADO->')