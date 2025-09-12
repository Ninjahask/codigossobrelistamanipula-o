with open("perfil.txt", "w") as arquivo:
    nome = input("digite o seu nome: ")
    arquivo.write(nome + "\n")
    idade = input("digite a sua idade: ")
    arquivo.write(idade + "\n")

with open("perfil.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
