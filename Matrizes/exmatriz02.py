matriz = []

l = int(input("LINHAS: "))
c = int(input("COLUNAS: "))

i = 0
while i < l:
    lista = []
    j = 0
    while j < c:
        num = int(input(f"Entrada de Dados \n Lin-{i} Col-{j}: "))
        lista.append(num)
        j += 1
    matriz.append(lista)
    i += 1

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1