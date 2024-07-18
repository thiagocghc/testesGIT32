cont = 0
num = int(input("Digite um número: "))
maior = num
menor = num

while cont < 10:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont = cont + 1
    num = int(input("Digite um número: "))

print("Maior: ",maior)
print("Menor: ",menor)