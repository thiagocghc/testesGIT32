i = 0
numeros = []
while i < 5:
    num = int(input("DIGITE UM NUMERO: "))
    numeros.append(num)
    i = i + 1

print(sum(numeros))
for num in numeros:
    print(num)