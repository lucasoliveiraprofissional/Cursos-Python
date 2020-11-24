'''Na verdade é aula017(Parte 2) - Listas, mas quis nomear assim.'''
teste= list()

teste.append('Gustavo')
teste.append(40)
print(teste)

galera= list()
galera.append(teste)

'''Como no exemplo antes da aula pratica,
o correto a se fazer nesse caso é:

galera.append(teste[:]) nas 2x que damos append'''

'''é possível dar print de apenas alguns dados separados da lista.
Neste caso por exemplo só o nome, ou só a idade.'''
galera= [['João',19],['Ana',33],['Joaquim',13],['Maria',45]]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')


'''É possível usar uma lista auxiliar e gravar esses dados dela
em uma lista fixa:'''

galera= list()
dado= list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))

    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')

