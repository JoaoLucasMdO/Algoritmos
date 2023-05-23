def calculo(totcab):
    totpes = y * 3 + 1
    pato = (4 * totcab - totpes) / 6
    coelho = totcab - pato
    return coelho, pato


y = int(input("Digite o número de cabeças: "))

print(f"O total de coelhos é: {calculo(y)}")

"""
cabeca = pato + coelho
pato = coelho - cabeca
coelho = cabeca - pato

pes = 2 * pato + 4 * coelho
pes = 2 * (coelho - cabeca) + 4 * coelho
pes = 2 * coelho - 2 * cabeca + 4 * coelho
pes = 6 * coelho - 2 * cabeca
pes = 6 * (cabeca - pato) - 2 * cabeca
pes = 6 * cabeca - 6 * pato - 2 * cabeca
pes = 4 * cabeca - 6 * pato
6 * pato + pes = 4 * cabeca
(4 * cabeca - pes) / 6 = pato 
"""
