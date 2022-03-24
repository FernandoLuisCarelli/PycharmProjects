import pandas as pd

precos = [1000, 1500, 1250, 2500]

def adicionar_imposto(preco):
    return preco * 1.1


precos_com_imposto = []
for preco in precos:
    precos_com_imposto.append(adicionar_imposto(preco))

print(precos_com_imposto)

preco_com_imposto2 = list(map(adicionar_imposto, precos))
print(preco_com_imposto2)

tabela = pd.read_excel("Base Vendas.xlsx")

tabela["Preco com Imposto"] = list(map(adicionar_imposto, tabela['Preco Unitario']))
tabela.to_excel("base vendas atualizada.xlsx")