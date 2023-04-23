# def par_impar(*args):
#     for item in args:
#         if item % 2 == 0:
#             print(f'{item} é par: ')
#         else:
#             print(f'{item} é impar: ')
            
# par_impar(1,2,3,4,5,6,7,8,9)

def par_impar(numero):
    verifica = numero % 2 == 0
    if verifica:
        return f'{numero} é par: '
    return f'{numero} é impar: '

result1 = par_impar(5)
result2 = par_impar(6)
result3 = par_impar(9)
print(result1)
print(result2)
print(result3)
