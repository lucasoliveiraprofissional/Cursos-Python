'''Leia o nome de uma pessoa e diga se ela tem SILVA no nome
porém nesse caso o Silva pode estar em qualquer lugar
creio que lá era o startswith mesmo'''

'''Ele pediu para que começássemos a usar o str
antes do input. Após ver o vídeo da solução do exercício22,
essa foi a alteração que fiz nesse código.'''

nome= str(input('Digite seu nome completo: '))

print(nome.capitalize().find('Silva'))

#mesmo principio do exercicio anterior, mesmo dilema