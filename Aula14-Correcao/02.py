def ehprimo(numero):
    divisoes = 0
    i = 1
    while i < numero:
        if(numero % i) == 0:
            divisoes += 1
        i += 1

        if divisoes == 2:
            return True
        else:
            return False


def total_primos(total):
    qtd = 0
    i = 2
    lista = []
    while qtd < total:
        if ehprimo(i):
            qtd += 1
            lista.append(i)
        i += 1
        return lista


qtd_primos = int(input("Digite a qtd de primos: "))
