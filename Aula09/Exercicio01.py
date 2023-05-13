vetor = []
for i in range(5):
    x = int(input(f"Digite o {i+1}°, valor: "))
    vetor.append(x)

vetor.sort()

print(vetor[::-1], "\n")

print(vetor)
