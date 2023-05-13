a = int(input("Digite um número inteiro: "))

if a%5 == 0:
    print(f"Seu número {a} é divisível por 5.")
    if a%3 == 0:
        print(f"Seu número {a} é divisível por 3 também.")
    else:
        print(f"Seu número {a} não é divísivel por 3.")

elif a%3 == 0:
    print(f"Seu número {a} é divísivel por 3 mas não por 5.")
