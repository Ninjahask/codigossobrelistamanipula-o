arquivo = open("compras.txt", "w")
arquivo.write("leite\n")
arquivo.write("detergente\n")
arquivo.write("Pão\n")
arquivo.close()

arquivo = open("compras.txt", "r")
conteudo = arquivo.read()
print(conteudo)