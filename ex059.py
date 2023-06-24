from time import sleep
n1 = int(input('\n\nDigite um número: '))
n2 = int(input('Digite outro número: '))
menu = 0
while menu != 5:
    print('\n\n')
    print('-='*10)
    print('''    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa''')
    print('-='*10)
    menu = int(input('O que você deseja: '))
    if menu == 1:
        print('A soma dos números é ', n1 + n2)
    elif menu == 2:
        print('O prodto dos números é ', n1 * n2)
    elif menu == 3:
        if n1 < n2:
            print('O maior número é ', n2)
        elif n1 > n2:
            print('O maior número é ', n1)
        else:
            print('Os números são iguais.')
    elif menu == 4:
        n1 = int(input('\n\nDigite um número: '))
        n2 = int(input('Digite outro número: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Resposta inválida!!!\n Tente novamente!!!')
    sleep(3)
print('Fim do programa.')