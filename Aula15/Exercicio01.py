arquivo = open("usuarios.txt")
texto = arquivo.read()

lista = texto.split('\n')
soma = 0
contador = 1
print("N°   Nome       Espaço Utilizado")
for i in lista:
    nome, numero = i.split(',')
    print(f"{contador}    {nome}    {numero}")
    contador += 1
    soma += int(numero)/1000000

media = soma / len(lista)
print(f"Espaço total ocupado: {soma:.2f} MB")
print(f"Espaço médio ocupado: {media:.2f} MB")
