import os
lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir , [d]eletar, [l]istar Itens: ')
    os.system('cls')

    if opcao == 'i':
        valor = input('Valor ?')
        lista.append(valor) 
        os.system('cls')

    elif opcao == 'd':
        if len(lista) == 0:
            print('Não existe item para deletar')
        else:

            try:

                indice_str = input('Digite o indice para excluir: ')
                indice = int(indice_str)
                del lista[indice]
            
            except ValueError:
                print('Valor não encontrado na lista: ')
            
            except IndexError:
                print('Indice não exite na lista: ')
            
            except Exception:
                print('Erro desconhecido: ')

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Não exite itens na lista: ') 
        else:
            for indice, valor in enumerate(lista):
                print(indice, valor)

    else:
        print('Escolha a opção correta: ') 

