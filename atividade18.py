try:
    with open('dados_secretos.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

except FileNotFoundError:
    print("Erro: O arquivo 'dados_secretos.txt' não foi encontrado.")