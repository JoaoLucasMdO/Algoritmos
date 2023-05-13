a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print("Os lados formam um triângulo!")
    if(a == b) and (b == c):
        print("Triângulo Equilátero!")
    elif(a == b) or (b == c) or (a == c):
        print("Triângulo Isóceles!")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")