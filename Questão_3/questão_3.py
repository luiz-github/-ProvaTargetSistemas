import json

with open('Questão_3/dadosQuestão_3.json', 'r') as file:
    data = json.load(file)

faturamento = data["faturamento"]
media = 0
valoresFAT = []
maiorMedia = 0

for i in faturamento:
    if faturamento != 0:
        media = media + i['valor']
        if i['valor'] != 0:
            valoresFAT.append(i['valor'])

media = media/len(valoresFAT)

for i in valoresFAT:
    if i > media:
        maiorMedia += 1

print(f'media: {media}')

print(f'Valor minimo: {min(valoresFAT)}')
print(f'Valor maximo: {max(valoresFAT)}')
print(f'Dias acima da média: {maiorMedia}')