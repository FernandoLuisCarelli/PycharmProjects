class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message
while True:
    try:
        x = int(input("entre com uma nota de 0 a 10: "))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10') #personalizando a excecao
        elif x < 0:
            raise InputError('Nota não pode ser negativa')
        break

    except ValueError:
        print('Valor invalido, deve-se digitar apenas numero.')
    except InputError as ex:
        print(ex)