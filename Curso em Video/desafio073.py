'''Crie uma tupla preenchida com os
20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na
ordem de colocacao. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem
alfabética.
C) Em que posição da tabela está o
time Chapecoense.'''

times= ('Atletico', 'Palmeiras', 'São Paulo', 'Santos', 'Athletico-PR', 'Chapecoense', 'Corinthians',
        'Ceará SC', 'Flamengo', 'Bahia', 'Goiás', 'Botafogo', 'Cruzeiro', 'Internacional', 'Fortaleza',
        'Grêmio', 'Avaí', 'Vasco da Gama', 'CSA', 'Fluminense')

#Perdi a f string, não estava aceitando os replaces que quis dar.
#Se eu coloco no print só do str( para frente ele aceita.

print('Os 5 primeiros times: ')
print(str((times[0:5])).replace("(", "").replace(")", "").replace("'", ""))
print('')

#Perdi a f string, não estava aceitando os replaces que quis dar.
#Se eu coloco no print só do str( para frente ele aceita.
print('Os últimos 4 times: ')
print(str(times[-4:]).replace("(", "").replace(")", "").replace("'", ""))
print('')
#só tive que confirmar como ele ia printar negativamente no video do Guanabara explicando
#eu estava fazendo [:-3]


print(f'Todos os times em ordem alfabética: {sorted(times)}')
print('')

'''Na hora de printar algo sorted, ele printa como se fosse
uma lista, ou seja, com []. O Guanabara disse que na aula
017 entenderemos o porque disso. Mas fica aqui a anotação.'''

'''Do modo que ele está, entre [] e com as aspas e vírgulas,
eu teria muito trabalho para fazer sumir essas coisas, uma vez
que o sorted não deve funcionar para tuplas, tendo em vista que
acontece isso.'''


'''Usando F Strings, no Python, para colocarmos o index de 
algo que seja uma String, temos que colocar esse algo entre
aspas ", senão o Python não entende. Como abaixo:'''

print(f'Posicao do Chapecoense: {times.index("Chapecoense")}')
print('')