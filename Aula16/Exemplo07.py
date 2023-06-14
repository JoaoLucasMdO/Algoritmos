def divisao(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as erro:
        return f"Ocorreu o problema: {erro}"
    except:
        return f"Ocorreu algum problema!"


n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
print(divisao(n1, n2))
