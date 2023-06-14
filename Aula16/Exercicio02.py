arquivo1 = open("carros.txt")
carro = arquivo1.readlines()
arquivo1.close()

arquivo2 = open("consumo.txt")
consumo = arquivo2.readlines()
arquivo2.close()

saida = open("saida.txt", "w", encoding="utf-8")

lista = []
menorconsumo = 0
preco = 2.25

for i in range(0, 5):
    carros = carro[i].strip("\n")
    consumos = consumo[i].strip("\n")
    custo = 1000 / float(consumos)
    gasto = custo * preco
    saida.write(f"Veículo {i+1}:\n")
    saida.write(f"Nome: {carros}\n")
    saida.write(f"Km por litro: {consumos}\n")
    saida.write(f"Custo: {custo:.2f}\n")
    saida.write(f"Gasto:{gasto:.2f}R$\n")
    saida.write("------------------------------\n")

    if consumo[i] > consumo[menorconsumo]:
        menorconsumo = i

saida.write(f"O menor consumo é: {carro[menorconsumo]}")
