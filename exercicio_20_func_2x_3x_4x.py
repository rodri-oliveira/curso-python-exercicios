def criar_cultiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = criar_cultiplicador(2)
print(duplicar(8))

triplicar = criar_cultiplicador(3)
print(triplicar(16))

quadriplicar = criar_cultiplicador(4)
print(quadriplicar(4))