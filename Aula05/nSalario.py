"""
Este programa calcula o novo salário 
tomando como base um reajuste de 15,3%
"""
#A variável salário é float pois 
#o salário pode ser não inteiro


salario = float(input("Digite o salário: "))
novo_salario = (salario * 1.153)
print("Novo Salário: ", novo_salario)