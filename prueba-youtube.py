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
