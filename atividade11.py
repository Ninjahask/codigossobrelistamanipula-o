with open("saudacao.txt", "w") as arquivo:

    arquivo.write("Ola mundo")

arquivo = open("saudacao.txt", "r")
conteudo = arquivo.read()
print(conteudo)