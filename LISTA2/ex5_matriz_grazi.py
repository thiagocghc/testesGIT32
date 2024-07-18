
matriz = [[1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1], 
          [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1], 
          [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1]]

for linha in matriz:
    print(linha)

while True:
    try:
        posicao = input(f'Digite a posição que quer marcar (no formato: linha,coluna): ')

        linha, coluna = posicao.split(',')
        linha = int(linha)
        coluna = int(coluna)

        matriz[linha][coluna] = 'X'

        print('=='*32)
        print(f"{'BATALHA NAVAL':^64}")
        print('=='*32)
    except:
        print("Entrada inválida!!!!!!!")


    for linha in matriz:
        for elemento in linha:
            print(f'[{elemento:^5}]', end='')
        print()
    print('=='*32)

   

