faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento = []
faturamento_total = 0

for key, value in faturamento_mensal.items():
    faturamento.append((key, value))
    faturamento_total += value

for elemento in faturamento:
    print(f"{elemento[0]}: {elemento[1]/faturamento_total * 100:.2f}%")


