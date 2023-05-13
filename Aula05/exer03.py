ano_nasc = int(input("Digite o ano de seu nascimento: "))
ano_atu = int(input("Digite o ano atual: "))
idade = ano_atu - ano_nasc
print(f"Idade: {idade} anos, {idade*12} meses, {idade*53} semanas e {idade*365} dias.")