lista = [1,10]

try:
    divisao = 10/0
    numero = lista[1]
    #x = a
except ZeroDivisionError:
    print('Não é possivel realizare uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print(ex)
else:
    print("Executa quando não ocorre excessão")
finally:
    print('Sempre continua executando')