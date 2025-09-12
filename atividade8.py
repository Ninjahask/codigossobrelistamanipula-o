with open("lembretes.txt", "r") as arquivo:
        primeira_linha = arquivo.readline()
        print(primeira_linha.strip())