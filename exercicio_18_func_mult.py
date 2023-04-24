def mult(*args):
    total = args[0]
    for item in args:
        total *= item 
    return total

result = mult(1,2,3)
print(result)

