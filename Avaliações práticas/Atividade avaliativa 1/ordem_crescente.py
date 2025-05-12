valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))
print('~'*20)
if valor1 == valor2:
    print('Valor 1 é igual ao Valor 2\n',
          f'{valor1} = {valor2}')
elif valor2 >= valor1:
    print('Valor 2 é maior que o Valor 1\n',
          f'{valor2} > {valor1}')
else:
    print('Valor 1 é maior que o Valor 2\n',
          f'{valor1} > {valor2}')

# Por que não funcionou desse jeito?

# if valor1 >= valor2:
#     print('Valor 1 é maior que o Valor 2\n',
#           f'{valor1} > {valor2}')
# elif valor2 >= valor1:
#     print('Valor 2 é maior que o Valor 1\n',
#           f'{valor2} > {valor1}')
# else:
#     print('Valor 1 é igual ao Valor 2\n',
#           f'{valor1} = {valor2}')
