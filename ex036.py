casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do sálario: R$'))
tempo = float(input('Digite em quantos anos vocẽ pretende pagar o empréstimo: '))

prestaçao = casa / (tempo * 12)
print('Para comprar uma casa de R${:.2f} em {:.2f} anos a prestação será de R${:.2f} ao mês.'.format(casa, tempo, prestaçao))
if prestaçao <= salario * (30/100):
    print('\033[1;32mEmpréstimo aprovado!')
else:
    print('\033[0331;31mEmpréstimo negado!')