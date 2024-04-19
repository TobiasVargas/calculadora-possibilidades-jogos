from random import randint
import itertools

# Cria uma matriz com todos os adversarios
adversarios = [
    ["Internacional", "Grêmio"], #1
    ["Flamengo", "Fluminense"],  #2
    ["Botafogo", "Vasco"],       #3
    ["Coritiba", "Juventude"],   #4
    ["Cruzeiro", "Fortaleza"],   #5
    ["Bahia", "Criciuma"],       #6
    ["Corinthians", "Vitória"],  #7
    ["Cuiabá", "Atlético MG"],   #8
    ["Criciuma", "Atlético PR"], #9
    ["Bragantino", "Goianense"]  #10
]

print("CALCULANDO POSSIBILIDADES")
print("\n")

# cria uma lista vazia de jogos
jogos = []
for adversario in range(0, len(adversarios)):
    # adiciona um codigo para cada conjunto de adversarios, ou seja, para cada jogo, e adiciona na lista de jogos
    jogos.append({"codigo": str(adversario), "times": adversarios[adversario], "resultados": []})

#cria uma lista de possibilidades de placares vazia
possibilidades = []

for jogo in jogos:
    # cria uma label para cada jogo. Exemplo: 0.Internacional x Grêmio
    label = jogo["codigo"] + "." + jogo["times"][0] + ' x ' + jogo["times"][1]
    possibilidade_vitoria_0 = label + ' = Vitória ' + jogo["times"][0]
    possibilidade_vitoria_1 = label + ' = Vitória ' + jogo["times"][1]
    possibilidade_empate = label + ' = Empate'
    # Gera as 3 possibilidades de uma partida: Vitória do time A, vitória do time B ou empate
    jogo["resultados"] = [possibilidade_vitoria_0, possibilidade_vitoria_1, possibilidade_empate]
    # Adiciona no dicionário de jogos
    possibilidades.append(possibilidade_vitoria_0)
    possibilidades.append(possibilidade_vitoria_1)
    possibilidades.append(possibilidade_empate)

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
