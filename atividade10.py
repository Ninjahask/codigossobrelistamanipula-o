with open("compras.txt", "r") as arquivo:
        for item in arquivo:
                item_limpo = item.strip()
                print(f"{item_limpo} (concluído)")