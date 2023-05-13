from random import randint
dado = [0] * 6
est = [0] * 6

for i in range(6000):
    x = randint(0, 5)
    dado[x] += 1

for i in range(6):
    est[i] = dado[i]/6000

for i in range(6):
    print(f"Lado {i+1} foi sorteado:{dado[i]}vezes = {est[i]:.2%}")
