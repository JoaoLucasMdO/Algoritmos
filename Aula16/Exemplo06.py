def entrada():
    try:
        num = int(input("Digite um número: "))
    except:
        return None
    else:
        return num
    finally:
        print("Fim da execução...")


print(entrada())
