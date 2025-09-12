lista = ['produto A, 100', 'produto B,250']

with open("vendas.txt", "w") as arquivo:
    for item in lista:
         arquivo.write(item + "\n")
                
print(lista)