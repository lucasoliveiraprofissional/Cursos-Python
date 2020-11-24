'''FAça um programa que leia o peso de 5
pessoas. No final, mostre qual foi o maior
e o menor peso lidos.'''

maior= 0
menor= 0

for c in range(0, 5):
    pesos= float(input('Digite seu peso: '))

    if c == 1:
        maior= pesos
        menor= pesos
    else:
        if pesos > maior:
            maior= pesos

        if pesos < menor:
            menor= pesos

'''nessa parte eu esqueci como faz o menor'''
'''Vi que depende do laço. Como nunca funcionou
if dentro de for comigo, fiquei meio desconfiado.'''

print('O menor peso foi {:.2f} e o maior peso foi {:.2f}'.format(menor, maior))