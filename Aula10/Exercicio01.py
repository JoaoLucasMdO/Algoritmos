
"""
x = 0
a = [0] * 10

while x < 10:
    print(f"Digite o {x+1}° número: ")
    a[x] = int(input())
    x += 1

a = a[::-1]

tuple(a)

print(a) """

t = ()

for i in range(5):
    x = int(input(f"Digite o {i+1}° número: "))
    t = t + (x,)

print(t[::-1])
