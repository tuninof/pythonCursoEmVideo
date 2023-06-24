n = int(input('Digite um número inteiro qualquer: '))
print('''\nEscolha uma das bases para a converção:\n
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL\n''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('\033[31mOpção invalida!!! Tente novamente.')