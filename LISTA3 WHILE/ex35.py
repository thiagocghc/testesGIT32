palavra = input("DIGITE ALGO: ").lower()
voagais = ['a','e','i','o','u']
consoantes = 0
vog = 0
for letra in palavra:
    if letra not in voagais:
        consoantes += 1
    if letra in voagais:
        vog += 1

print("TOTAL DE CONSOANTES: ",consoantes)
print("TOTAL DE VOGAIS: ",vog)
