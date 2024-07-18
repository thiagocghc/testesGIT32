####CONTADORES
brancos = 0
nulos = 0
ana = 0
bia = 0
cris = 0
duda = 0
total = 0

while True:
    print("Eleições 2024")
    print("Favor escolha sua Candidata!!!")
    print(" 1 - ANA \n 2 - Bia \n 3 - Cris \n 4 - Duda")
    print(" 5 - Branco \n 6 - Nulo")
    voto = int(input("Digite seu voto: "))
    if voto == 0:
        break
    total += 1
    if voto == 1:
        ana += 1
    elif voto == 2:
        bia += 1
    elif voto == 3:
        cris += 1
    elif voto == 4:
        duda += 1
    elif voto == 5:
        brancos += 1
    elif voto == 6:
        nulos += 1
    else:
        nulos += 1


porcentagembrancos = (brancos/total) * 100
print("TOTAL DE VOTOS: ",total)
print(f"Total \n Ana: {ana} \n Bia: {bia} \n Cris: {cris} \n Duda: {duda} \n Brancos: {brancos} \n Nulos: {nulos} ")
print("VOTOS NULOS: ", (nulos/total) * 100," %")
print("VOTOS BRANCOS: ", porcentagembrancos, " %")
    

