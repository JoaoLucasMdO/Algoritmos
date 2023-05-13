a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))



if a + b > c or a + c > b or b + c > a:
    print("Os lados formam um triângulo!")
    if a == b and a == c:
        print("É um triângulo equilátero.")
    if a == b and a != c or a == c and a!= b or b == c and b != a:
        print("É um triângulo isósceles.")
    if a != b and a!=c and b != c:
        print("É um triângulo escaleno")
