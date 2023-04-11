

while True:
    primeiro_numero = input('Digite o primeiro numero: ')
    segundo_numero = input('Digite o primeiro segundo: ')
    operador = input('Digite o operador:  + ou - ou * ou / ')
    
    numeros_validos = None
    resultado = 0

    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Numero(s) incorreto(s) ')
        continue

    operadores_validos = '+-*/'

    if operador not in operadores_validos:
        print('Operador invalido: ')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador: ')
        continue

    if operador == '+':
        resultado = primeiro_numero_float + segundo_numero_float
    elif operador == '-':
        resultado = primeiro_numero_float - segundo_numero_float
    elif operador == '*':
        resultado = primeiro_numero_float * segundo_numero_float
    else:
        resultado = primeiro_numero_float / segundo_numero_float
    print(f'O resultado da operação de {operador} é {resultado}')






        


    sair = input('Quer sair? [s]im ').lower().startswith('s')
    print(sair)

    if sair:
        break
    

