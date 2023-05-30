def cercado(cabecas, pes):
    c = (pes - 2 * cabecas) / 2
    p = cabecas - c
    return p,c


total_cabecas = int(input("Digite o total de Cabeças: "))
total_pes = int(input("Digite o total de pés: "))

patos, coelhos = cercado(total_cabecas, total_pes)

print(f"O total de coelhos é {coelhos}, o total de patos é {patos}")
