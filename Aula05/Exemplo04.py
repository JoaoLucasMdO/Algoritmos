t1 = float(input("Digite a primeira nota: "))
t2 = float(input("Digite a segunda nota: "))
t3 = float(input("Digite a terceira nota: "))

media = (t1 + t2 + t3)/3

if media<3:
    print("Reprovado")
elif media<7:
    print("Exame")
    nota = 12 - media
    print(f"Você precisa tirar no mínimo nota: {nota:.1f}")
else:
    print("Aprovado")

