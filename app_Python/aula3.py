# a = int(input('Primeiro Valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior numero é :{} '.format(a))
# elif b > a and b > c:
#     print('O maior numero é :{} '.format(b))
# else:
#     print('o maior numero é: {}'.format(c))
#
# print('Final do programa')

# a = int(input('Entre com um valor: '))
# b = int(input('Entre com um valor: '))
#
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um numero PAR')
# else:
#     print('Nenhum numero par foi digitado')

nota1 = int(input('Digite uma nota 1: '))
if nota1 > 10:
    nota1 = int(input('Digite uma nota 1: '))

nota2 = int(input('Digite uma nota 2: ' ))
if nota2 > 10:
    nota2 = int(input('Digite uma nota 2: '))

nota3 = int(input('Digite uma nota 3: '))
if nota3 > 10:
    nota3 = int(input('Digite uma nota 3: '))

nota4 = int(input('Digite uma nota 4: '))
if nota4 > 10:
    nota4 = int(input('Digite uma nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(media)

# if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
#     print('Media: {}'.format(media))
# else:
#     print('Alguma nota foi digitada errada :')