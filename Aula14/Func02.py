from Func01 import prim


def contprim(n):
    contador = 0
    for i in range(1, n+1):
        if prim(i) == True:
            contador += 1
    return contador
