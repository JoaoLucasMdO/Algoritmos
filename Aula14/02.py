from Func01 import prim
from Func02 import contprim

y = int(input("Digite o número do RA: "))

lista = []

for i in range(1, y + 1):
    if prim(i) == True:
        lista.append(i)

soma = sum(lista)

print(f"Os números são:{lista} A soma deles é {soma} A quantidade de números primos é : {contprim(y)}")

