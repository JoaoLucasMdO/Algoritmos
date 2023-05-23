import math
n = str(input("Digite  RA: "))
soma = 0
mult = 1
for i in range(0, len(n)):
    soma += int(n[i])
    if int(n[i]) == 0:
        continue
    mult *= int(n[i])

print(f"A soma dos digitos do RA é: {soma}, A multiplicação é: {mult}")
