def prim(x):
    contador = 0
    i = 1
    while i <= n:
        if n % i == 0:
            contador += 1

        i += 1

    if contador == 2:
        return True
    else:
        return False


n = int(input("Digite o numero a ser verificado: "))

if prim(n) == True:
    print(f"O número {n} é Primo ")
else:
    print(f"O número {n} não é Primo")
