num = int(input("DIGITE UM NÚMERO: "))
while num < 2:
    num = int(input("DIGITE UM NÚMERO: "))

i = num
cont = 0
while i >= 1:
    if num % i == 0:
        print(i)
        cont += 1
        i = i - 1
    i = i - 1

if cont == 2:
    print(f"{num} é primo!")
else:
    print(f"{num} Não é Primo!!")