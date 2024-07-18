ze = 1.60
chico = 1.70
anos = 0
while ze <= chico:
    chico += 0.02
    ze += 0.03
    anos += 1

print(f"QUANTIDADE DE ANOS: {anos:.2f}")
print("ALTURA FINAL DO ZÉ: ",ze)
print("ALTURA FINAL DO CHICO: ",chico)