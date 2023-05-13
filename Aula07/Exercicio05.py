while True:
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    if base > 0 and altura > 0:
        break
    print("Nenhum dos dois valores poder ser menor que zero\n")

print(f"\nA área do triângulo é {(base * altura) / 2:.2f}")
