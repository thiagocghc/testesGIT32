cont = 1
numerador = 1
s = 0
while cont <= 50:
    s += numerador / cont
    print(f"Loop {cont} Valor: {s}")
    numerador += 2
    cont += 1

print(f"TOTAL: {s:.3f}")