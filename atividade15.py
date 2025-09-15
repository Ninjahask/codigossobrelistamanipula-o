termo_de_busca = input("Digite um termo de busca: ")

with open('buscas.log', 'a') as arquivo_log:
    arquivo_log.write(termo_de_busca + '\n')

print(f"O termo '{termo_de_busca}' foi registrado em buscas.log.")