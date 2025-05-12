ctn = 0
inicio = int(input("Início: "))
for ygona in range(inicio, -1, -1):
    if inicio <= 0:
        break
    print(ygona)
    ctn += 1
print(ctn)