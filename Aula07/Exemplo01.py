soma = 0
for x in range(1,11):
    idade = int(input(f"Digite a {x}a. idade: "))
    if x == 5:
        continue
    soma = soma + idade



media = soma / x
print(f"A média das idades é igual a {media:.2f}")