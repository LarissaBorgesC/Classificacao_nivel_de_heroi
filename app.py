


nome = input("Nos informe seu nickname: ")

xp = float(input("Nos informe seu xp: "))

while True:

    if xp < 1000:
        nivel = "ferro"
        break

    elif 1000.01 < xp < 2000:
        nivel = "bronze"
        break

    elif 2000.01 < xp < 5000:
        nivel = "prata"
        break

    elif 5000.01 < xp < 7000:
        nivel = "ouro"
        break

    elif 7000.01 < xp < 8000:
        nivel = "platina diamante"
        break

    elif 8000.01 < xp < 9000:
        nivel = "ascendente"
        break

    elif 9000.01 < xp < 10000:
        nivel = "radiante"
        break

    else:
        nivel = "radiante"
        break

print(f"O héroi de nome {nome} esta no nivel {nivel}!")
