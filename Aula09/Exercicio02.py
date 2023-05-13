vetor1 = [0] * 3
vetor2 = [0] * 3
vetor3 = []

'''for i in range(3):
    vetor1[i] = int(input(f"Digite o {i+1}°, valor do vetor1: "))
    vetor2[i] = int(input(f"Digite o {i+1}°, valor do vetor2: "))
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])'''

for i in range(3):
    vetor1[i] = int(input(f"Digite o {i+1}°, valor do vetor1: "))

for i in range(3):
    vetor2[i] = int(input(f"Digite o {i+1}°, valor do vetor2: "))
    
for i in range(3):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])


print(vetor3)
