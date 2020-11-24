'''Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação(opcional)

Adicione também as docstrings da função.
'''

'''Fiz a versão b pois queria ver como ele solucionaria.'''


def notas(*n, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r= dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['média'] >= 7:
            r['situacao'] = 'BOA'
        if r['média'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


#Programa principal:
resp= notas(5.5,2.5,9,8.5)
print(resp)
help(notas)

'''O *n dentro do def significa que ele receberá
várias notas, não somente uma.'''
'''Muito interessante o modo como ele fez a media e a soma'''