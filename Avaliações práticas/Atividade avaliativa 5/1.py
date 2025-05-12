frase = input('Cê quer qual vogal mais de repete?\n'\
      'Digite um texto aqui: ')
i = 0
vg_a = 0
vg_e = 0
vg_i = 0
vg_o = 0
vg_u = 0
print(f'Contando... \n {frase}')
while i < len(frase):
    letra = frase[i]
    if letra == 'a':
        vg_a += 1
    if letra == 'e':
        vg_e += 1
    if letra == 'i':
        vg_i += 1
    if letra == 'o':
        vg_o += 1
    if letra == 'u':
        vg_u += 1
    i += 1
print(f'a -> {vg_a}\n'
      f'e -> {vg_e}\n'
      f'i -> {vg_i}\n'
      f'o -> {vg_o}\n'
      f'u -> {vg_u}\n')