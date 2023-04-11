nome = 'Luis Otavio'

tamanho_str = len(nome)

contador = 0
nova_str = ''

while contador < len(nome):
    nova_str += f'*{nome[contador]}'
    contador += 1
print(nova_str)