diario = input("Digite a sua nova entrada de diario: ")

with open("diario.txt", "a") as arquivo:
        arquivo.write(diario + "\n")

import datetime
print(str(datetime.datetime.now()))