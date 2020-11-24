'''Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome SANTO
eu creio que nesse caso temos que usar o startswith que eu descobri
e relatei abaixo. Pois no próximo exercicio, a palavra que
ele quer encontrar pode estar em qualquer lugar da variavel
'''

'''Ele pediu para que começássemos a usar o str
antes do input. Após ver o vídeo da solução do exercício22,
essa foi a alteração que fiz nesse código.'''

cidade= str(input('Digite o nome de sua cidade: '))

print(cidade.capitalize().find('Santo'))


#não quero que ele printe SANTO, quero que ele printe Santo, porém
#não sei se nessa sintaxe vai funcionar
#quero que ele procure pela palavra depois que ela estiver
#to upper, mas que na hora de printar, digite Santo
#dá para fazer com o find também, mas tenho que fazer com que a frase assuma um
#formato unico, ou td maiusc ou td minusc, ou pelo capitalize para poder achar algo dentro de seu conteudo
#dá para fazer com o find, dá para fazer com o replace, que terá a função do upper ou lower
#print(('Santo') in cidade, '\n')

#Não sai no resultado que eu quero, porém já é algo. O correto é usar
#o método startswith, dentro de uma condição if. Não estou usando condições if.
#gostaria de converter essa resposta que tenho do find para uma string, sem precisar usar
#if
#vi alguns códigos já, mas vou esperar para fazer junto com o prof
