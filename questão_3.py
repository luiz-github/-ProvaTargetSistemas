import json

with open('dadosQuestão_3.json', 'r') as file:
    data = json.load(file)

faturamento = data["faturamento"]
media = 0
valoresFAT = []

for i in faturamento:
    if faturamento != 0:
        media = media + i['valor']
        if i['valor'] != 0:
            valoresFAT.append(i['valor'])


print(f'media: {media}')

print(f'Valor minimo: {min(valoresFAT)}')
print(f'Valor maximo: {max(valoresFAT)}')