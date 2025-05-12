Sexo = input('Digite "H" para homem e "M" para mulher: ')
Altura = float(input('Altura: '))
if Sexo == 'H':
    print(f'{(72.7 * Altura) - 58:.2f}')
else:
    print(f'{(62.1 * Altura) - 44.7:.2f}')