'''Leia o nome de uma pessoa e diga se ela tem SILVA no nome
porém nesse caso o Silva pode estar em qualquer lugar'''

'''Fazendo de acordo com o Guanabara
Ele quis que colocássemos o str antes do input.
Quis fazer assim pois eu acho que a resolução dele será muito melhor'''

nome= str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))

