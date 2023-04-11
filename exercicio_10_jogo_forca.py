palavra_secreta = 'rodrigo'
letras_acertadas = ''
numero_tentativas = 0
tamnho_palavra = len(palavra_secreta)
acertos = 0

while True:
    
    letra_digitada = input(f'Digite a letra: ')

    if len(letra_digitada) > 1:
        print(f'Voce digitou mais de uma letra: ({letra_digitada}) digite novamente: ')
        continue

    if letra_digitada in palavra_secreta:
        print(f'Voce acertou:')
        acertos += 1
        letras_acertadas += letra_digitada
    else:
        print(f'Voce errou:') 
        
    numero_tentativas += 1
    print(f'Numero de tentativas {numero_tentativas}x')

    if acertos == tamnho_palavra:
        print(f'Voce venceu: a palavra é {palavra_secreta}')
        break


    if numero_tentativas >= 10:
        print(f'Numero de tentativas esgotada: {numero_tentativas}x')
        break
    