numeros = []
pares = []
impares = []

i = 0
while i < 20:
    num = int(input("Digite um número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    i = i + 1

print("LISTA DE NUMEROS DIGITADOS: ",numeros)
print("TOTAL DE NUMEROS DIGITADOS: ",sum(numeros))
print("TOTAL DE PARES: ",pares)
print("TOTAL DE IMPARES: ",impares)