'''Crie um programa que leia vários números
inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles
(desconsiderando o flag)'''

'''Copiei a versão dele já de cara pois fiquei
mais de uma semana sem treinar Python'''

soma = cont = 0

while True:
    num= int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    #tem que ser desse modo, antes dele chegar a somar, tem
    #que cortar o barato dele, não pode deixar ele chegar a
    #somar. Por isso esse if vem antes.
    cont += 1
    soma += num

print(f'A soma dos {cont} valores foi: {soma}')
