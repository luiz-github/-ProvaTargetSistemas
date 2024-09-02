import json

with open("questão_4/questão_4.json", "r") as faturamento:
    data = json.load(faturamento)

data = data["faturamento"]

total = sum(item["valor"] for item in data)

def percentualEstado(data, total):
    x = (data * 100)/total
    return x

for i in data:
    print(f"Unidade {i["estado"]}: {round(percentualEstado(i["valor"], total), 2)}%")
        

    