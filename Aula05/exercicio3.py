from math import pow, sqrt
x1 = float(input("Digite o x1: "))
y1 = float(input("Digite o y1: "))
x2 = float(input("Digite o x2: "))
y2 = float(input("Digite o y2: "))
dx = x2 - x1
dy = y2 - y1
d = sqrt(pow(dx,2) + pow(dy,2))
print("Distância = ", d)
