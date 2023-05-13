valor = float(input("Digite a hora: "))
hora = int(valor)
minutos = (valor - hora) * 100
minutos_totais = (hora*60) + minutos
print(f"Total em minutos: {minutos_totais}")
