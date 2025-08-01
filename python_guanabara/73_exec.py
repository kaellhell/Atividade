classificacao_brasileirao_2024 = (
    'Botafogo', 'Flamengo', 'Atlético-MG', 'Grêmio', 'Palmeiras',
    'São Paulo', 'Fluminense', 'Internacional', 'Corinthians', 'Cruzeiro',
    'Fortaleza', 'Vasco da Gama', 'Red Bull Bragantino', 'Athletico-PR', 'Cuiabá',
    'Bahia', 'Vitória', 'Juventude', 'Criciúma', 'Atlético-GO'
)

print('\033[32mOs cinco primeiros colocados são:\033[0m')
print(f'- {classificacao_brasileirao_2024[:5]}')
print('\033[33mOs quatro últimos colocados são:\033[0m')
print(f'- {classificacao_brasileirao_2024[-4:]}')
print('\033[34mTimes em ordem alfabética:\033[m')
print(f'- {sorted(classificacao_brasileirao_2024)}')
print('\033[35mPosição do Atlético-MG:\033[0m')
print(f'- {classificacao_brasileirao_2024.index("Atlético-MG")+1}ª posição')