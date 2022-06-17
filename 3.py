from random import randint

faturamento = []
media = 0
maior = 0
menor = 9000
dias = 0

for dia in range(0, 22):
    faturamento.append(randint(2200, 3400))  # atribui valor aleatorio para cada dia útil do mês

for dia in faturamento:
    media += dia
    if dia > maior:
        maior = dia
    if dia < menor:
        menor = dia

media /= len(faturamento)

for dia in faturamento:
    if dia > media:
        dias += 1

print(f"""Menor valor de faturamento ocorrido no mês: {menor}
Maior valor de faturamento ocorrido no mês: {maior}
Número de dias no mês em que o valor do faturamento diário foi superior à média mensal: {dias}""")
