#Fernanda Lemes Cacho
#Exercicio 4
import json

menor = 1000000.0
maior = 0.0
k=0
soma=0.0

with open("dados-ex4.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)


for i in dados:
    
    soma = soma + i['valor'];

for i in dados:
    percentual=i['valor']*100.00/soma

    print(i['estado'], percentual)
