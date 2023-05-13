
Sex = input("Digite se você se identifica como 'Homem' ou 'Mulher': " )
H = float(input("Digite sua altura: "))
   
if Sex == "Homem":
    print(f"Seu peso ideal é {(72.7*H)-58:.1f}kg")   
elif Sex == "Mulher":
    print(f"Seu peso ideal é {(62.1*H)-44.7:.1f}kg")

