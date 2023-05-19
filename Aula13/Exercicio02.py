def triangular(n):
    for a in range(3, n + 1):
        if a * (a - 1) * (a - 2) == n:
            return True

    return False


x = int(input("Digite o número a ser verificado: "))

print(f"O número {x} é: {triangular(x)}")
