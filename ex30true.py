maior = 0
menor = 999999999
while True:
    num = int(input("Digite um numero: "))
    if num < 0:
        break
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(maior)
print(menor)