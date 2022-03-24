a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b


# print('soma : ' + str(soma))
# print('subtracao : ' + str(subtracao))
# print('multiplicacao : ' + str(multiplicacao))
# print('divisao : ' + str(divisao))
# print('resto : ' + str(resto))

print('soma: {soma}. \nSubtracao: {subtracao}. \nMultiplicacao: {multiplicacao}. \nDivisao: {div}. \nResto: {resto}'
      .format(soma=soma, subtracao=subtracao, multiplicacao=multiplicacao, div=divisao, resto=resto))