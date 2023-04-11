numero = int(input('Digite o numero: '))
newList = []
for n in range(3, numero + 1):
    primo = True
    for div in range(2, n):
        if n % div == 0:
            primo = False
            break
    if primo:
        newList.append(n)

print(newList)
        



