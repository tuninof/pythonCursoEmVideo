velocidade = float(input('Qual é a velocidade do carro? '))
multa = (velocidade - 80)*7

if velocidade > 80.0:
    print('Você excedeu o limite de velocidade!!!! Sua multa será de ${} reais'. format(multa))
else:
    print('Boa viagem, dirija com segurança!!!')