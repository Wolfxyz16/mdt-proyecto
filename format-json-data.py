import json
import pandas as pd

# Cargar archivo JSON
with open("datos-etiquetados.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)  # Carga como lista de diccionarios

datos_relevantes = []

for item in datos:
    comentario = item["data"]["comment"]
    etiqueta = item["annotations"][0]["result"][0]["value"]["choices"][0]

    if etiqueta == 'Relevant':
        datos_relevantes.append({
            "comentario": comentario,
            "etiqueta": None
        })

print(f"Tenemos {len(datos_relevantes)} datos relevantes.")

with open("comentarios-buenos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_relevantes, archivo, ensure_ascii=False, indent=4)
    print(f"Se ha guardado el archivo {archivo.name}")

pd.DataFrame(datos_relevantes).to_csv("comentarios.csv", index=False, encoding="utf-8")  
