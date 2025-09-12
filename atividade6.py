novo_lembrete = input("Digite seu novo lembrete: ")

with open("lembretes.txt", "a") as arquivo:
        arquivo.write(novo_lembrete + "\n")