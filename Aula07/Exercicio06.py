while True:
    x = int(input("Digite um número: "))
    if x >= 0:
        break
    print("O valor deve ser maior que zero")

if (x == 0) or (x == 1):
    fatorial = 1
else:
    fatorial = 1
    for i in range(1,x+1):
        fatorial *= i

print(f"O fatoraial de {x}! é igual a {fatorial}")