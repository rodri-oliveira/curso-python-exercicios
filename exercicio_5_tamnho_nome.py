nome = input('Dgite seu nome: ')

nome_tamanho = len(nome)

if nome_tamanho >= 3 and nome_tamanho <= 6:
    print(f'O nome {nome} é normal:')
elif nome_tamanho < 3:
    print(f'O nome {nome} é curto:')
else:
    print(f'O nome {nome} é grande demais: ')