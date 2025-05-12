qnt_valor = 0
soma = 0
maior_20 = 0
while True:
    valor = float(input('Valor: '))
    if valor == 0:
        break
    if valor >= 20:
        maior_20 += 1
    qnt_valor += 1
    soma += valor
print('Total de valores digitados: ',qnt_valor)
print('Soma dos valores: ',soma)
print(soma/qnt_valor)
print('Valores maiores que 20: ',maior_20)
#"A única pessoa que pode simpatizar com você e entendê-lo é você.
# Então, seja bom consigo mesmo."