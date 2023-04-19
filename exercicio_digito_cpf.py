import re
import sys
nove_digitos = 0
# entrada_cpf = input('Digite seu cpf: ')

# limpando a string com REGEX 

while True:
    entrada_cpf = input('Digite seu cpf: ')
    entrada_eh_sequencial = entrada_cpf == entrada_cpf[0] * len(entrada_cpf)
    if entrada_eh_sequencial:
        print(f'A entrada {entrada_cpf} não é valida: ')
        continue
    else:
        # SEM REGEX
        # cpf = '215.809.658-60' \
#         .replace('.', '') \
#         .replace('-', '') \
#         .replace(' ', '')
        # com REGEX
        cpf_limpo = re.sub(r'[^0-9]','', entrada_cpf)
        nove_digitos = cpf_limpo[:9]
        dez_digitos = cpf_limpo[:10]

        acc_1 = 0
        acc_2 = 0

        multiplicador_1 = 10
        multiplicador_2 = 11

        for item in nove_digitos:
            acc_1 += int(item) * multiplicador_1
            multiplicador_1 -= 1

        for item in dez_digitos:
            acc_2 += int(item) * multiplicador_2
            multiplicador_2 -= 1

        resultado_1 = (acc_1 * 10) % 11
        resultado_2 = (acc_2 * 10) % 11

        resultado_1 = resultado_1 if resultado_1 <= 9 else 0
        resultado_2 = resultado_2 if resultado_2 <= 9 else 0

        verifica_cpf = nove_digitos + str(resultado_1) + str(resultado_2)
        if verifica_cpf == cpf_limpo:
            print(f'O CPF {verifica_cpf} é valido: ')
        else:
            print(f'O CPF {verifica_cpf} não é valido: ')


 






































