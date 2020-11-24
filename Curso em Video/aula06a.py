import emoji

n = input('Digite algo: ')
numerico = (n.isnumeric())
alfanumerico = (n.isalnum())
letras = (n.isalpha())

if numerico == True:
    print('{} é numérico'.format(n))
else:
    if alfanumerico == True:
        print('{} é alfanumérico'.format(n))
    else:
        if letras == True:
            print('{} é string'.format(n))
        else:
            print('Essa bosta não é merda nenhuma!')
