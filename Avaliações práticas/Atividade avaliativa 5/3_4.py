sm = 0
for numero in range(1, 500+1, 1):
    if numero % 2 != 0:
        if numero % 3 == 0:
            print(numero)
            sm += numero
print(sm)