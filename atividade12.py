with open("cadastro.csv", "w") as arquivo:
    nome = input("digite o seu nome: ")
    email = input("digite o seu email: ")
    arquivo.write(f"{nome}, {email}\n")