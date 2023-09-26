lista = [1,2,3,4,5,6,7,8,9,10]
alvo = 7


def busca_binaria(lista, alvo):
    baixo, alto = 0, len(lista) -1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        
        elemento = lista[meio]
        
        if elemento == alvo:
            return meio
        elif elemento < alvo:
            baixo = meio + 1
        else:
            alto = meio -1
    return -1

resultado = busca_binaria(lista, alvo)

if resultado != -1:
    print(f'O elemento {alvo} foi encontrado na posição {resultado}')
else:
    print(f'O elemento {alvo} não foi encontrado')