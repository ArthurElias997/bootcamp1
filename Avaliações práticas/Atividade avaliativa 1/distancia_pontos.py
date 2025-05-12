xp = float(input('Posição X do ponto P: '))
yp = float(input('Posição Y do ponto P: '))
xq = float(input('Posição X do ponto Q: '))
yq = float(input('Posição Y do ponto Q: '))
import math
dpq = math.sqrt((xp - xq)**2 + (yp - yq)**2)
print(
    '~'*20, '\n'
    f'Ponto P: ({xp}, {yp})\n'
    f'Ponto Q: ({xq}, {yq})\n'
    f'a distância entre os pontos é de: {dpq:.2f}'
)