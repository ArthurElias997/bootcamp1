a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
if a >= b + c or b >= a + c or c >= a + b:
    print('Não é um triângulo.\n'
          'Todos os lados precisam ter a medida menor que a soma das '
          'medidas dos outros dois lados.')
else:
    if a == b == c:
        print('É um triângulo equilátero')
    elif a == b or a == c or b == c:
        print('É um triângulo isósceles')
    else:
        print('É um triângulo escaleno')