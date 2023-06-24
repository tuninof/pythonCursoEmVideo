from datetime import date
data = date.today().year
ano = int(input('Ano de nascimento: '))
idade = data - ano


print('Quem nasceu em {} tem {} anos em 2022'.format(ano, idade))
if idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para seu alistamento'.format(saldo))
    alistamento = data + saldo
    print('Seu alistamento será em {}'.format(alistamento))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    alistamento = data - saldo
    print('Seu alistamento foi em {}'.format(alistamento))
else:
    print('Você deve se alistar imediatamente!')