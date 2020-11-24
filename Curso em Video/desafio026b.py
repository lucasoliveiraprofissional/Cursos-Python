'''Faça um programa que leia uma frase e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição aparece a primeira vez
- Em que posição ela aparece a ultima vez '''

'''Fazendo de acordo com o Guanabara
Ele quis que colocássemos o str antes do input.
Quis fazer assim pois eu acho que a resolução dele será muito melhor

eu usei o upper em todos os formats, sendo que só precisava usar uma vez
só, assim como eu só uso uma vez só o strip, e foi o que ele fez
'''

frase= str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes nessa frase.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
#para o leigo que não entende que o vetor inicia do 0, colocamos como se iniciasse
#do 1, por isso o +1 depois do A

print('A letra A aparece pela última vez na posição {}.'.format(frase.rfind('A')+1))
#o rfind quer dizer: procure a partir da direita, right, ele colocou rfind como eu

