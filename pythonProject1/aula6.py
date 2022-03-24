conjunto = {1, 2, 3, 4}
conjunto2 = {6, 7, 8, 9, 1, 2}

conjunto_novo = conjunto.union(conjunto2)  # uniao entre dois conjuntos
conjunto_novo1 = conjunto.intersection(conjunto2) # pega somente os valores que se repetem nos conjuntos
conjunto_diferenca = conjunto.difference(conjunto2) # mostra somente os valores que sao diferentes em comparação dos conjuntos
conjunto_diferenca2 = conjunto2.difference(conjunto)
conjunto_dif_assimetrica = conjunto.symmetric_difference(conjunto2) #apresenta a diferenca entre um e outro, mostrando primeiro de um conjunto depois do outro

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_a.issubset(conjunto_b) # funcao que verifica se um conjunto esta dentro do outro.
conjunto_superset = conjunto_b.issuperset(conjunto_a) # funcao que verifica se é um super conjunto


print(conjunto_novo)
print(conjunto_novo1)
print(conjunto_diferenca)
print(conjunto_diferenca2)
print(conjunto_dif_assimetrica)
print(conjunto_subset)
print(conjunto_superset)