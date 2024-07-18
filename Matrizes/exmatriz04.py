numeros = [11,12,13,25,26,27,29,30,31]

matriz = []
i = 0
pos = -1
while i < 3:
    lista = []
    j = 0
    while j < 3:
        num = numeros[pos]
        lista.append(num)
        pos -= 1
        print("POS: ",pos)
        j += 1
    matriz.append(lista)
    i += 1

x = 0 
while x < len(matriz):
    print(matriz[x])
    x += 1