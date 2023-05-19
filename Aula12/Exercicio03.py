def prim(x):
    lista = []

    for a in range(1, n+1):
        contador = 0
        i = 1
        while i <= a:
            if a % i == 0:
                contador += 1

            i += 1

        if contador == 2:
            lista.append(a)

    return lista


n = int(input("Digite o Limite: "))

print(prim(n))

"""
i, p = 2, 0
coluna = 1
while p <= 50:
    
    if prim(i):
        print(i, end=" - ")
        n += 1
        coluna += 1
    i += 1
    
    if coluna > 15:
        print()
        coluna = 1"""
