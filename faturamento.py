import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

faturamento = [dia['valor'] for dia in dados]

# menor faturamento
menor_faturamento = min(faturamento)

# maior faturamento
maior_faturamento = max(faturamento)

# média do faturamento excluindo dias sem faturamento
media_faturamento = sum(faturamento) / len([dia for dia in dados if dia['valor'] > 0])

# número de dias com faturamento acima da média
dias_acima_da_media = len([dia for dia in dados if dia['valor'] > media_faturamento])

print(f'Menor faturamento: R$ {menor_faturamento:.2f}')
print(f'Maior faturamento: R$ {maior_faturamento:.2f}')
print(f'Média de faturamento (excluindo dias sem faturamento): R$ {media_faturamento:.2f}')
print(f'Número de dias com faturamento acima da média: {dias_acima_da_media}')