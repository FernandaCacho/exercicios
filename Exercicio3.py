#Fernanda Lemes Cacho
#Exercicio 3

import json

menor = 1000000.0
maior = 0.0
k=0
media=0.0
with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)


for i in dados:
    if (i['valor']!=0):
        media = media + i['valor'];
        k=k+1;
        if(i['valor']<menor):
            menor=i['valor'];
        if(i['valor']>maior):
            maior=i['valor'];

          
media = media/k

print("O menor valor de faturamento: ",menor);
print("O maior valor de faturamento: ",maior);
print(f"O valor medio de faturamento: ",media);

