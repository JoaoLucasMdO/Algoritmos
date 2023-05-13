compra = float(input("Digite o valor da compra: "))

if compra<=1000.00:
    print(f"O seu desconto é 10% totalizando um valor de {compra - (compra * (10/100)):.2f}")
elif compra<=5000.00:
    print(f"O seu desconto é 20% totalizando um valor de {compra - (compra * (20/100)):.2f}")
elif compra>5000.00:
    print(f"O seu desconto é 30% totalizando um valor de {compra - (compra * (30/100)):.2f}")
