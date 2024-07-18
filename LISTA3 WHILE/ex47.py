somadosquadrados = 0
soma = 0
i = 1
while i <= 10:
    somadosquadrados += i ** 2
    soma += i
    i += 1

diferenca = (soma ** 2) - somadosquadrados
print(diferenca)
