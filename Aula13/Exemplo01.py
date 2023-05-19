def fatorial(n):
    if n > 1:
        return n * fatorial(n - 1)
    else:
        return 1


n = int(input("Digite o valor de n: "))

print(fatorial(n))

