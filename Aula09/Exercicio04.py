indice = 0
numero = [0] * 10
prim = False
x = 101
qtd = 0

while qtd < 10:
    div = 0
    for i in range(1, x):

        if (x % i) == 0:
            div = div + 1


    if div == 1:
        prim = True


    if prim:
        numero[indice] = x
        indice = indice + 1
        qtd = qtd + 1
    x = x+1

print(numero)
