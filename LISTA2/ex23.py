num = int(input("Digite um number: "))
i = num
lista = []

while i > 1:
    i = i - 1
    if num % i == 0:
        lista.append(i)

print(sorted(lista))
print(sum(lista))
