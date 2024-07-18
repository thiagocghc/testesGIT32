cont = 0
lista = []
while cont <= 100:
    cont = cont + 1
    if cont % 2 == 0:
        lista.append(cont)

print(lista)
print(sum(lista))