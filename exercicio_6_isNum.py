num = input('Digite um numero inteiro: ')



if num.isdigit():
    verifica_int = int(num)
    par_impar = verifica_int % 2 == 0
    if par_impar:
        print(f'O numero {num} é PAR: ')
    else:
        print(f'O numero {num} é impar: ')
else:
    print(f'O numero {num} não é um numero inteiro: ')


# try:
#     entrada_int = int(num)
#     numero_par = entrada_int % 2 == 0
#     par_impar_texto = 'IMPAR'
#     if numero_par:
#         print(f'O numero {entrada_int} é PAR: ')
#     else:
#         print(f'O numero {entrada_int} é {par_impar_texto}')

# except:
#     print(f' {num} não é um numero inteiro: ')
