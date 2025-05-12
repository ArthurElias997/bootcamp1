# celsius = ((float(input('Fahreinheit: ')) - 32) / 1.8)
inicio = int(input('Fahreinheit início: '))
fim = int(input('Fahreinheit final: '))
if inicio < fim:
    for fahreinheit in range(inicio, fim+1, 1):
        celsius = (fahreinheit - 32) / 1.8
        print(f"{fahreinheit} ºF | {celsius:.3f} ºC",)
if inicio > fim:
    for fahreinheit in range(inicio, fim-1, -1):
        celsius = (fahreinheit - 32) / 1.8
        print(f"{fahreinheit} ºF | {celsius:.3f} ºC",)