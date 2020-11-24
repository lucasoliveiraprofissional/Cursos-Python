'''Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome SANTO
eu creio que nesse caso temos que usar o startswith que eu descobri.
Pois no próximo exercicio, a palavra que
ele quer encontrar pode estar em qualquer lugar da variavel
'''

'''Fazendo de acordo com o Guanabara
Ele quis que colocássemos o str antes do input.
Quis fazer assim pois eu acho que a resolução dele será muito melhor'''

cid= str(input('Em que cidade você nasceu? ')).strip()
print(cid.capitalize()[:5] == 'Santo')
#porque a palavra santo tem 5 letras só e vamos começar verificando desde o indice 0 do vetor
#capitalizei para deixar igual a String que estamos usando para comparar

#Genial ser só isso! Genial!