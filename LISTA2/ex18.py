
quant = int(input("Digite a quantidade de numeros a serem lidos: "))
maior = 0
i = 0
while i < quant:
    num = int(input("Digite um numero: "))
    if num > maior:
        maior = num
    i = i + 1

print("MAIOR: ",maior)