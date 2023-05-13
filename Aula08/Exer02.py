data = input("Digite a data nesse formato -> dd/mm/aaaa: ")

# data = data.split('/')

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

nova_data = ano+mes+dia

print(nova_data)



