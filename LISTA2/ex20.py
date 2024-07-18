#EX20
num = int(input("DIGITE UM NUMERO: "))
lidos = 0 #LIDOS
pares = 0
while num != 0:
    lidos += 1
    if num % 2 != 1:
        print(f" {num} é par!!!")
        pares += 1
    else:
        print(f" {num} NÃO é par!!!")
    num = int(input("DIGITE OUTRO NUMERO: "))

print("TOTAL DE NUMBERS LIDOS: ",lidos)
print("TOTAL DE PARES: ",pares)