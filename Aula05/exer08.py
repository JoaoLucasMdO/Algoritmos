qw = float(input("Digite a quantidade de quilowatt: "))
salario = float(1302.00)
custo_qw = salario/8
conta = custo_qw * qw
con_resi = custo_qw * qw
print(f"O valor de cada quilowatt é R$:{custo_qw:.2f}")
print(f"O valor a ser pago pela residêcia é {con_resi:.2f} com desconto é {con_resi - con_resi * (15/100)}")