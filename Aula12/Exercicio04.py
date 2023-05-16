def anobi(n):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


a = int(input("Digite o número no formato AAAA: "))
print(anobi(a))
