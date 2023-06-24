distancia = float(input('Qual a distância da sua viagem em km? '))
if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print('O valor da sua passagem é de ${:.2f} reais'.format(passagem))
