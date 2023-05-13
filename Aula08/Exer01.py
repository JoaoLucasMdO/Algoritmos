nome = input("Digite seu nome: ")
nome_meio = input("Digite seu nome do meio: ")
nome_ultimo = input("Digite seu sobrenome: ")

nome_completo = (nome + " " + nome_meio + " " + nome_ultimo)

print(f"{nome_completo}")

# Criptografia

nome_cripto = ''

for indice in range(0,len(nome_completo)):
    nome_cripto += chr(ord(nome_completo[indice])+1)

print(f"{nome_cripto}")






