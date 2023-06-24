primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite sua razão: '))
termos = primeiro
while termos < primeiro + 10 * razao:
    print(termos, end=' ')
    termos += + razao
print('Fim')