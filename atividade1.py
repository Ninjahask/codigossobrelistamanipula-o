arquivo = open("saudacao.txt", "w")
arquivo.write("Ola mundo")
arquivo.close()

arquivo = open("saudacao.txt", "r")
conteudo = arquivo.read()
print(conteudo)