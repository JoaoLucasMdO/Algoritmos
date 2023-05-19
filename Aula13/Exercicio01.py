from Funcao01 import rand

Tdnv = "S"
Vitorias = 0
Derrotas = 0
Empates = 0
while Tdnv != "N":
    input("Aperte ENTER para começar: ")
    a = rand()

    print(f"Seu número é {a}")

    b = rand()

    print(f"O número do computador é {b}")

    if a > b:
        print("Você venceu!")
        Vitorias += 1

    elif a == b:
        print("Empate!")
        Empates += 1

    else:
        print("Você perdeu")
        Derrotas += 1

    print(f"V:{Vitorias} D:{Derrotas} E:{Empates}")

    Tdnv = input("Quer jogar de novo? Digite N para sair: ")
