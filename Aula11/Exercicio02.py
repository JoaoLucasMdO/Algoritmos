d1 = {}
for i in range(5):
    nome = input(f"Entre com o {i+1}º nome: ")
    idade = int(input(f"Entre com a {i+1}ª idade: "))
    d1[nome] = idade

soma = 0

for idade in d1.values():
    soma += idade

media = soma / len(d1)
print(f"A média das idades é {media}")

for nome, idade in d1.items():
    if idade > media:
        print(f"{nome} tem {idade} anos!")
