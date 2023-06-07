def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
multiplicacao_por_dez = criar_funcao(multiplicacao, 10)
print(soma_com_cinco(23))
print(multiplicacao_por_dez(23))