a = 10
b = 20
soma = a + b
print(soma)
print('Resultado da soma é : ' + str(soma))

def teste_funcao():
    print('ola mundo')

def fazendo_sozinho(numero1, numero2):
    resultado = numero1 + numero2
    print(resultado)

def unindo(texto1, texto2):
    result_texto = texto1 + texto2
    print(result_texto)

def entrada(valor1, valor2):
    somadeles = valor1 + valor2
    print(somadeles)

if __name__ == '__main__':
    teste_funcao()
    fazendo_sozinho(1, 5 )
    unindo('Fernando ', 'Nunes')
    val1 = int(input('Digite primeiro valor:'))
    val2 = int(input('Digite segundo valor:'))
    entrada(val1, val2)