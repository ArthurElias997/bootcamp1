qnt_aluno = 0
aprovado = 0
reprovado = 0
while True:
    nota = float(input('Nota: '))
    if nota == -1:
        break
    if nota >= 5:
        aprovado += 1
    else:
        reprovado += 1
    qnt_aluno += 1
print('alunos reprovados: ',reprovado)
print('alunos aprovados: ',aprovado)
print('Total de alunos que fizeram a prova: ',qnt_aluno)
#"A única pessoa que pode simpatizar com você e entendê-lo é você.
# Então, seja bom consigo mesmo."