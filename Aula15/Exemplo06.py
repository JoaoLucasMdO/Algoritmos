with open("frutas.txt", "a", encoding="utf-8") as arquivo:
    while True:
        fruta = input("Digite um texto: ")
        if fruta == 'sair':
            break
        else:
            arquivo.write(fruta)
            arquivo.write("\n")