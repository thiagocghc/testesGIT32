matriz = [[1,2,3,4,5],[9,5,6,7,8],[9,8,7,6,5],[1,2,3,4,5]]
nova_matrix = []

i = 0
while i < len(matriz):
    j = 0
    linha = []
    while j < len(matriz[i]):
        x = matriz[i][j] * 5
        linha.append(x)
        j += 1
    nova_matrix.append(linha)
    i += 1

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1

print()
print("#"*30)

y = 0
while y < len(nova_matrix):
    print(nova_matrix[y])
    y += 1
