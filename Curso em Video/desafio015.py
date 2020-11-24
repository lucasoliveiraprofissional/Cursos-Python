#Aluguel de carros
#R$60 por dia e R$0.15 por Km rodado

dias= int(input('Quantos dias alugados? '))
km= float(input('Quantos Km rodados? '))

print('O total a pagar é de R${:.2f}'.format((dias*60)+(km*0.15)))

#nesse momento, a lógica está fácil, então por isso eu posso fazer monolitico o format e o procedimento.