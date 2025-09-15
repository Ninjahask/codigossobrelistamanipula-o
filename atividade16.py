def verificar_arquivo(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r'):
            pass  
        print(f"O arquivo '{nome_do_arquivo}' existe!")
        
    except FileNotFoundError:
        print(f"O arquivo '{nome_do_arquivo}' não foi encontrado.")

verificar_arquivo("exemplo_inexistente.txt")

verificar_arquivo("vendas.txt")