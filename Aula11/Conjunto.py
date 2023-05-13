lista1 = [0] * 5
lista2 = [0] * 5
i = 0
for i in range(5):
    lista1[i] = int(input(f"Digite o {i+1}º da lista 1: "))
    lista2[i] = int(input(f"Digite o {i + 1}º da lista 2: "))

c1 = set(lista1)
c2 = set(lista2)

c3 = c1.union(c2)

print(c3)


