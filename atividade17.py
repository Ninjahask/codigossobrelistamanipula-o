numeros = []
resultado = None

try:
    with open('numeros.txt', 'r') as arquivo:
        for linha in arquivo:
            numeros.append(int(linha.strip()))
    numero1 = numeros[0]
    numero2 = numeros[1]
    try:
        resultado = numero1 / numero2
        print(f"O resultado da divisão de {numero1} por {numero2} é: {resultado}")
    except ZeroDivisionError:
        print("Divisão por zero não é permitida.")
except FileNotFoundError:
    print("Erro: O arquivo 'numeros.txt' não foi encontrado.")
except (ValueError, IndexError):
    print("Erro: O arquivo 'numeros.txt' não contém dois números válidos.")