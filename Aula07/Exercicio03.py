n = int(input("Digite um numero inteiro positivo: "))
a = 0
b = 1

for i in range(1, n):
    print(b)
    a,b = b, a + b
