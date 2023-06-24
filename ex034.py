print('Analizador de triângulos')
print('\n')
a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))
if a < b + c and b < a + c and c < a + b:
    print('Esses seguimentos formam um triângulo.')
else:
    print('Esses seguimentos não podem formar um triângulo.')