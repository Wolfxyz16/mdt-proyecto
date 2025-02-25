# Proyecto Mineria de Datos Textuales

## 1. Formular una pregunta de investigación relacionada con el análisis de emociones que se pueda investigar en una red social (Mastodon, Facebook, etc.)
* ¿Qué emociones aparecen más en las redes sociales cuando se habla de inmigración?
* Cuando se habla de ChatGPT, ¿qué emoción surge más en Mastodon: miedo, esperanza, tristeza o alegría?


## 2. Formular una o más consultas para obtener los datos para responder a la pregunta y obtencion de los datos.

Para obtener los datos que nos ayudarán a responder a las preguntas vamos a ejecutar el siguiente script que nos ayudará a obtener datos sobre el proyecto:

```python
import time
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

data = []
youtube_video_url = "https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s"

# Indicar la ruta del chromedriver usando Service
service = Service(r'/bin/chromedriver')

# Iniciar el navegador con la ruta al chromedriver
with Chrome(service=service) as driver:
    wait = WebDriverWait(driver, 15)
    driver.get(youtube_video_url)
    
    # Esperar a que el video cargue y que el body sea accesible
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

    # Hacer scroll para cargar comentarios
    for item in range(200):  # Cambia el rango si necesitas más interacciones de scroll
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)  # Deja tiempo para que los comentarios se carguen

    # Esperar a que los comentarios sean visibles
    comments = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text")))

    # Extraer los comentarios
    for comment in comments:
        data.append(comment.text)

# Convertir a DataFrame
df = pd.DataFrame(data, columns=['comment'])

# Mostrar los primeros 5 comentarios
print(df.head())
```

Con los datos ya guardados en un objeto `DataFrame` lo podemos almacenar fácilmente como un archivo `csv` en local.

```python
import
```

## 3. Preprocesamiento y anonimización de los datos.
* Tener en cuenta que, dependiendo de sus datos, es posible que sea necesario eliminar/agregar algunos pasos al preprocesamiento y que es importante adecuar el preprocesamiento al modelo concreto que usamos.

## 4. Anotar el conjunto de datos (test) para evaluar un modelo
* Elegir las etiquetas adecuadas para responder a la pregunta de investigación.
* Usar LabelStudio para anotar los datos
* Guardar en formato json

## 5. Dado que no tendrá un conjunto de datos para entrenar un modelo, os aconsejamos usar uno o más de las siguientes opciones:
* Crear un enfoque basado en el léxico
* O crear un conjunto de datos de plata usando emoji/palabras de emoción como pseudoetiquetas (distant supervision)
* Finalmente, también puedes utilizar el aprendizaje por transferencia (transfer learning) si encuentras conjuntos de datos adecuados en otro idioma.

## 6. Evaluar el modelo, usando la métrica adecuada que corresponde a la tarea.

