n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Média do aluno é {}.'.format(media))
if media < 5:
    print('Aluno reprovado!!!')
elif 7 > media >= 5:
    print('Aluno em recuperação!!')
else:
    print('Aluno aprovado!!!')
