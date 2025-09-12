with open("perfil.txt", "r") as arquivo:
    nome = arquivo.readline().strip()

    idade = int(arquivo.readline().strip())

    print(f"o seu nome é {nome}, e sua idade e {idade}")
