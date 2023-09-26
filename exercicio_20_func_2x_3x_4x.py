def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = criar_multiplicador(2)
print(duplicar(8))

triplicar = criar_multiplicador(3)
print(triplicar(16))

quadriplicar = criar_multiplicador(4)
print(quadriplicar(4))