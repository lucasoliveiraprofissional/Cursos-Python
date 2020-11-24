'''Crie um programa qonde o usuário digite
uma expressão qualquer que use parenteses.
Seu aplicativo deverá analisar se a expressão
passada está com os parenteses abertos e fechados
na ordem correta.'''

'''Fiz a versão b pois não tinha ideia de como
elaborar uma logica para isso.'''

expr= str(input('Digite uma expressao com parenteses: '))
pilha= []

'''Cada ez que um parenteses abrir, ele vai jogar dentro
da pilha.'''

#simb é de simbolo
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        pilha.append(')')
        if len(pilha) > 0:
            pilha.pop()
        else:
            #se a pilha estiver vazia, ele fecha os parenteses
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')


'''Do lado de fora, aqui, ele verifica se a pilha está 
cheia ou vazia.
Cada vez que ele abre um parenteses, ele vai adicionando
um parenteses na pilha.
Cada vez que eu encontrar um parenteses fechando,
eu removo um que abriu anteriormente, para fazer par
com esse que fechou.
Se a pilha estiver vazia, ele coloca um parenteses fechando,
é o ultimo else, aí dá erro, ele espera que de o erro,
quer dizer que não tem par de parenteses por ai'''

'''Se o len da pilha for zero, quer dizer que cada parentese
aberto teve seu par para fechar.'''

