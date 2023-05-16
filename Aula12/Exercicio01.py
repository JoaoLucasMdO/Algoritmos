def parimpar(x):
    if x % 2 == 0:
        resultado = True
    else:
        resultado = False

    return resultado


n = int(input("Digite o numero a ser verificado: "))

if parimpar(n) == True:
    print(f"O número {n} é Par.")
else:
    print(f"O número {n} é Impar")

"""print(f"O número é par? --> {parimpar(n)}")"""

