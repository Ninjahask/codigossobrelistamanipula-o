entradas_diario = []

with open("diario.txt", "r") as arquivo:
    for linha in arquivo:
         linha_limpa = linha.strip()
         if linha_limpa:
                entradas_diario.append(linha_limpa)
                
print(entradas_diario)