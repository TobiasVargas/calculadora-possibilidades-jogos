from random import randint
import itertools

# Cria uma matriz com todos os adversarios

adversarios = [
    [
        {
            "time": "Internacional",
            "probabilidade": 50
        },
        {
            "time": "Grêmio",
            "probabilidade": 50
        }
    ],
    [
        {
            "time": "Flamengo",
            "probabilidade": 30
        },
        {
            "time": "São Paulo",
            "probabilidade": 70
        }
    ],
    [
        {
            "time": "Palmeiras",
            "probabilidade": 10
        },
        {
            "time": "Corinthians",
            "probabilidade": 90
        }
    ],
    [
        {
            "time": "Atlético-MG",
            "probabilidade": 80
        },
        {
            "time": "Fluminense",
            "probabilidade": 20
        }
    ],
    [
        {
            "time": "Santos",
            "probabilidade": 35
        },
        {
            "time": "Athletico-PR",
            "probabilidade": 65
        }
    ]
]

print("CALCULANDO POSSIBILIDADES")
print("\n")

jogos = []
for adversario in range(0, len(adversarios)):
    # adiciona um codigo para cada conjunto de adversarios, ou seja, para cada jogo, e adiciona na lista de jogos
    jogos.append({"codigo": str(adversario), "times": adversarios[adversario], "resultados": []})

#cria uma lista de possibilidades de placares vazia
possibilidades = []

for jogo in jogos:
    label = jogo["codigo"] + "." + jogo["times"][0]["time"] + ' x ' + jogo["times"][1]["time"] + " = "
    jogo_provavel = jogo["times"]
    probabilidade_maior = ""
    if jogo_provavel[0]["probabilidade"] > jogo_provavel[1]["probabilidade"]:
        probabilidade_maior = label + "Vitória " + jogo_provavel[0]["time"]
        possibilidades.append(probabilidade_maior)
    elif jogo_provavel[1]["probabilidade"] > jogo_provavel[0]["probabilidade"]:
        probabilidade_maior = label + "Vitória " + jogo_provavel[1]["time"]
        possibilidades.append(probabilidade_maior)
    else:
        probabilidade_maior = label + "Empate"
        possibilidades.append(probabilidade_maior)
        probabilidade_maior = label + "Vitória " + jogo_provavel[0]["time"]
        possibilidades.append(probabilidade_maior)
        probabilidade_maior = label + "Vitória " + jogo_provavel[1]["time"]
        possibilidades.append(probabilidade_maior)

# Obtendo todas as combinações de possibilidades. Usa a biblioteca itertools
combinacoes = list(itertools.combinations(possibilidades, len(jogos)))

# Gera o contador de combinações de jogos possíveis (rodadas)
combinacao_valida = 0
for combinacao in combinacoes:
    primeiros_caracteres = []
    for caracteres in range(0, len(jogos)):
        primeiros_caracteres.append(combinacao[caracteres][0])
    primeiros_caracteres_sem_repeticao = list(set(primeiros_caracteres))
    if len(primeiros_caracteres_sem_repeticao) == len(jogos):
        # Verifica se todas as combinações contem jogos diferentes. Para não correr o risco de combinar mais de um resultado para a mesma partida
        combinacao_valida = combinacao_valida + 1
        print("COMBINAÇÃO " + str(combinacao_valida))
        print(combinacao)
        print("\n")
