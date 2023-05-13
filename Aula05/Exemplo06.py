media = int(input("Digite a média: "))

if media >= 5:
    if media == 10:
        print("Aprovado com louvor")
    else:
        if media >= 8:
            print("Aprovado com mérito")
        else:
            if media >=6:
                print("Aprovado com destaque")
else:
    print("Reprovado")