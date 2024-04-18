from random import randint
import itertools

adversarios = [["Internacional", "Grêmio"], ["Flamengo", "Fluminense"], ["Botafogo", "Vasco"], ["Coritiba", "Juventude"]]

jogos = []
for adversario in range(0, len(adversarios)):
    jogos.append({"codigo": str(adversario), "times": adversarios[adversario], "resultados": []})

print(jogos)

possibilidades = []

for jogo in jogos:
    label = jogo["codigo"] + "." + jogo["times"][0] + ' x ' + jogo["times"][1]
    possibilidade_vitoria_0 = label + ' = Vitória ' + jogo["times"][0]
    possibilidade_vitoria_1 = label + ' = Vitória ' + jogo["times"][1]
    possibilidade_empate = label + ' = Empate'
    jogo["resultados"] = [possibilidade_vitoria_0, possibilidade_vitoria_1, possibilidade_empate]
    possibilidades.append(possibilidade_vitoria_0)
    possibilidades.append(possibilidade_vitoria_1)
    possibilidades.append(possibilidade_empate)

elementos = possibilidades

# Obtendo todas as combinações de elementos
combinacoes = list(itertools.combinations(elementos, len(jogos)))

# Imprimindo as combinações
combinacao_valida = 0
for combinacao in combinacoes:
    primeiros_caracteres = []
    for caracteres in range(0, len(jogos)):
        primeiros_caracteres.append(combinacao[caracteres][0])
    primeiros_caracteres_sem_repeticao = list(set(primeiros_caracteres))
    if len(primeiros_caracteres_sem_repeticao) == len(jogos):
        combinacao_valida = combinacao_valida + 1
        print("COMBINAÇÃO " + str(combinacao_valida))
        print(combinacao)
        print("\n")
