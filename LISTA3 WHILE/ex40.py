inicial = int(input("INICIAL: "))
final = int(input("FINAL: "))

soma = 0

if inicial > final:
    print("Intervalo Inválido!!")
else:
    while inicial <= final:
        if inicial % 2 == 1:
            soma += inicial
            print(inicial)
        inicial += 1
    print(soma)