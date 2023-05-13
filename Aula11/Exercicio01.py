idades = {
    'ana': 34,
    'pedro': 31,
    'josé': 45,
    'joão': 18
}

maior = 0
chave_maior = ''

for nome in idades.keys():
    if len(nome) > maior:
        maior = len(nome)
        chave_maior = nome

print(f"O maior numero de caracteres é {maior}, pertence ao {chave_maior} e sua"\
      f" idade é {idades.get(chave_maior)}")

