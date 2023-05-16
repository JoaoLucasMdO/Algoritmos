def conversor(h=0, m=0, s=0):
    n1 = h * 3600
    n2 = m * 60
    return n1 + n2 + s


lista = []
horario = input("Digite o horario no formato HH:MM:SS --> ")
lista = horario.split(":")
h = int(lista[0])
m = int(lista[1])
s = int(lista[2])
print(conversor(h, m, s))
