n = int(input('\n\n\033[1;35m      Digite um número: '))
n1 = n % 2
if n1 > 0:
    print('\n\033[31mO número {} é ímpar'.format(n))
else:
    print('\n\033[32mO número {} é par'.format(n))

