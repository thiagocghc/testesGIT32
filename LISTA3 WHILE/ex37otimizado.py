import math

num = int(input("DIGITE UM NUMERO: "))
i = 2
cont = 0
while i <= math.sqrt(num):
    if num % i == 0:
        cont = cont + 1
        print(i)
    i = i + 1

print(cont)
if cont == 0:
    print(f"{num} não é primo!!")
else:
    print(f"{num} é primo!!")

