print('Digite os números que serão operados')
num1 = float(input('Número: '))
if num1 == str:
    print('Apenas números')
else:
    num2 = float(input('Número: '))
    if num2 == str:
        print('Apenas números')
    else:
        op = input('\nSoma +\n'
                   'Subtração -\n'
                   'Multiplicação *\n'
                   'Divisão /\n'
                   'Escolha a operação aritmética: ')
        if op != '+' and op != '-' and op != '*' and op != '/':
            print(op, 'Não é válido')
        else:
            if op == '+':
                print(f'{num1} {op} {num2} = {num1 + num2:.2f}')
            elif op == '-':
                print(f'{num1} {op} {num2} = {num1 - num2:.2f}')
            elif op == '*':
                print(f'{num1} {op} {num2} = {num1 * num2:.2f}')
            else:
                print(f'{num1} {op} {num2} = {num1 / num2:.2f}')