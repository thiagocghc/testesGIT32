num = int(input("DIGITE UM NUMERO: "))
maior = num
menor = num

while num > 0:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input("DIGITE UM NUMERO: "))

print("Maior: ",maior)
print("Menor: ",menor)
