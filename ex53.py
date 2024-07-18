i = 0
imc = 0
fem = 0
masc = 0
alturas = 0

idade = int(input("IDADE: "))
sexo = input("SEXO: ")
peso = float(input("PESO: "))
altura = float(input("ALTURA: "))

maisvelho = idade
maisnovo = idade
maisalto = altura
maisbaixo = altura
maiorpeso = peso

while i <= 3:
    if idade > maisvelho:
        maisvelho = idade
    if idade < maisnovo:
        maisnovo = idade
    if altura > maisalto:
        maisalto = altura
    if altura < maisbaixo:
        maisbaixo = altura
    if peso > maiorpeso:
        maiorpeso = peso
    
    alturas += altura
    imc += peso / (altura * altura)

    if sexo == "F" or sexo == "f":
        fem += 1
    if sexo == "M" or sexo == "m":
        masc += 1

    i += 1
    idade = int(input("IDADE: "))
    sexo = input("SEXO: ")
    peso = float(input("PESO: "))
    altura = float(input("ALTURA: "))

print(f"Mais velho {maisvelho}")
print(f"Mais novo {maisnovo}")
print(f"Mais alto {maisalto}")
print(f"Mais baixo {maisbaixo}")
print(f"Mais pesado {maiorpeso}")

porfeminino = (fem / i) * 100
pormasc = (masc / i) * 100
mediaalturas = alturas / i
mediaimcs = imc / i

print(" Porcentagem SEXO FEM ",porfeminino)
print(" Porcentagem SEXO MAS ",pormasc)
print(" Média das Alturas ",mediaalturas)
print(" Média dos IMCs ",mediaimcs)

print("VALOR DE I ",i)