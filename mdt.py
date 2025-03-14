import pandas as pd
import json

"""
Debido a la falta de coordinación al principio del grupo, los tres integrantes hemos acabado etiquetando cosas diferentes.
    * Carre ha etiquetado TODOS los comentarios con [POS], [NEG], [NEU], [IRR].
    * Yeray ha etiquetado TODOS los conmentarios con [REL], [IRR].
    * Iker ha etiquetado los comentarios [REL] de Yeray con [POS], [NEG], [NEU].

En este script lo que hacemos es juntar las etiquetas de Yeray e Iker para poder 
"""

# Cargamos los comentarios scrapeados
with open('data/yeray-labeled.json', 'r', encoding='utf-8') as file:
    yeray_data = json.load(file)

with open('data/iker-labeled.json', 'r', encoding='utf-8') as file:
    iker_data = json.load(file)

iker_new_data = []
pos_iker_data = 0

for line in yeray_data:
    id = line['id']
    comment = line['data']['comment']
    sentiment = line['annotations'][0]['result'][0]['value']['choices'][0]

    print(f"id: {id}")
    print(f"comment: {comment}")
    print(f"sentiment: {sentiment}")

    # Si el sentimiento es relevante tendremos que mirar la etiqueta de Iker
    if sentiment == 'Relevant':
        iker_comment = iker_data[pos_iker_data]['data']['comment']
        iker_sentiment = iker_data[pos_iker_data]['annotations'][0]['result'][0]['value']['choices'][0]
        if iker_comment == comment:
            sentiment = iker_sentiment
        pos_iker_data += 1

    iker_new_data.append({
        "id": id,
        "comment": comment,
        "sentiment": sentiment
    })
