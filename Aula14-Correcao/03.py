numero = input("Digite o numero: ")
soma = 0
mult = 1
for i in numero:
    soma += int(i)
    mult *= int(i)

print(f"Soma:{soma} Multiplicação: {mult}")
