from random import randint
computador = randint(0, 5) #faz o computador pensar
print('\n')
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('\n')
jogador = int(input('Em que numero eu pensei? ')) #jogador tenta adivinhar
print('\n')
if jogador == computador:
     print('Parabéns!!! Você acertou!!!')
else:
    print('Errou!!! Eu pensei no número {} e não no número {}'.format(computador, jogador))
print('\n')
print('\n')
