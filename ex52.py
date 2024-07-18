listanotas = []
nome = input("ATLETA: ")

while len(listanotas) < 7:
    nota = float(input("NOTA: "))
    listanotas.append(nota)
    print(listanotas)


print(listanotas)   
listanotas.remove(max(listanotas))
listanotas.remove(min(listanotas))
print(listanotas)   
print("Atleta: ",nome)
print("Média: ",sum(listanotas) / len(listanotas))