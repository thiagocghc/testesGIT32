cont = 0
soma = 0
while cont < 10:
    num = int(input("digite um numero: "))
    if num > 0:
        soma = soma + num
    cont = cont + 1


media = soma / cont
print("MEDIA: ",media)