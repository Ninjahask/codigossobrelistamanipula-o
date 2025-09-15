total_vendas = 0

with open('vendas.txt', 'r') as arquivo:
    for linha in arquivo:
        valor_venda = float(linha.strip())
        print(f"R$ {valor_venda:.2f}")
        total_vendas += valor_venda

print(f"\n---")
print(f"Total de vendas: R$ {total_vendas:.2f}")