import random

nove_digitos = ''
for item in range(9):
    nove_digitos += str(random.randint(0, 9))

acc_1 = 0
multiplicador_1 = 10

for item in nove_digitos:
    acc_1 += int(item) * multiplicador_1
    multiplicador_1 -= 1
resultado_1 = (acc_1 * 10) % 11
resultado_1 = resultado_1 if resultado_1 <= 9 else 0

dez_digitos = ''
dez_digitos = nove_digitos + str(resultado_1)

multiplicador_2 = 11
acc_2 = 0

for item in dez_digitos:
    acc_2 += int(item) * multiplicador_2
    multiplicador_2 -= 1
resultado_2 = (acc_2 * 10) % 11
resultado_2 = resultado_2 if resultado_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}-{resultado_1}{resultado_2}'

print(cpf_gerado_pelo_calculo)


 






































