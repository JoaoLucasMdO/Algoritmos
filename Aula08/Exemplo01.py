nome = input("Digite seu nome: ")
data = input("Digite a data dd/mm/aaaa: ")

print(f"Olá {nome}, tenha uma excelente noite!!")

print(type(nome))

print(len(nome))

print(nome[::-1])

print(nome.count('o'))

novo_nome = nome.replace('a', '@').replace('A', '@')

print(novo_nome)

novo_nome = novo_nome.strip()

print(novo_nome.split())

print(data.split('/'))

print(novo_nome)

print(novo_nome.lower().title())






