soma_par = 0
qnt_par = 0
soma_impar = 0
qnt_impar = 0
while True:
    num = int(input('Valor: '))
    if num == 0:
        break
    else:
        if num % 2 == 0:
            soma_par += num
            qnt_par += 1
        else:
            soma_impar += num
            qnt_impar += 1
if qnt_impar == 0 and qnt_par == 0:
    print('Nenhum valor foi digitado')
elif qnt_par == 0:
    print(f'Média dos números ímpares: {soma_impar/qnt_impar:.2f}')
elif qnt_impar == 0:
    print(f'Média dos números pares: {soma_par/qnt_par:.2f}')
else:
    print(f'Média dos números pares: {soma_par/qnt_par:.2f}')
    print(f'Média dos números ímpares: {soma_impar/qnt_impar:.2f}')
