# Documentación 

## ¿Qué opinan los espectadores de medios de comunicación alternativos sobre el nuevo formato de la Liga de Campeones?

El fútbol europeo ha sufrido un gran cambio este año. La competición más seguida del mundo entero, la Liga de Campeones de la UEFA, estrenó un nuevo formato donde entre otras cosas se amplian los equipos participantes a treinta y seís. Estos cambios han generado opiniones polarizadas en los espectadores. A su vez estas opiniones han ido cambiando a lo largo que se ha ido desarrollando el torneo, yendo de negativas a positivas. Sin embargo, todavía existen un gran bloque de retractores.

En este proyecto vamos a analizar las **opiniones de espectadores de medios de comunicación alternativos sobre el nuevo formato de la Liga de Campeones**, con la inteción de conocer si este nuevo formato es aceptado entre los seguidores de esta competición. Para ello vamos a extraer la información de la sección de comentarios de los vídeos de analísis de medios de comunicación como la media inglesa.

## Extracción de datos

Una vez bien definida la pregunta de investigación con la que trabajaremos, nuestro primer objetivo sera conseguir un conjunto de datos adecuado. Para la obtención de los datos usaremos el script del archivo 'prueba-youtube.py'. Mediante este script, utilizando la libreria webdriver y el ejecutable chromedriver leeremos los comentarios del video que deseamos y crearemos el inicio de la base de datos. 

Como primera idea, decidimos extraer comentarios de distintos videos de medios de comunicación diferentes para obtener mas variedad de datos. Sin embargo, debido a que la cantidad de datos que se extrajeron con un solo video nos parecio suficiente, scrappear mas datos.

```Video
    https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s
```

Una vez ejecutado el script, obtuvimos un conjunto de 464 comentarios no etiquetados. Una vez analizado el conjunto de datos, se ha dicidio emplear las siguientes etiquetas:

```Guia de anotación
   - **Positivo**: Se asignará la etiqueta positivo a un comentario si en este se expresa una opinión favorable sobre el nuevo formato de la Liga de Campeones. Puede incluir elogios, satisfacción o argumentos que justifiquen el cambio de formato.  
    *Ejemplo: "A mi el nuevo formato me encanta, buen vídeo cracks! Por cierto el directo de ayer divertidísimo"*  

    - **Negativo**: Se asignará esta etiqueta a un comentario si este expresa una opinión de rechazo sobre el nuevo formato de la Liga de Campeones. Puede incluir críticas, descontento o argumentos que expliquen por qué el cambio no les parece correcto.  
      *Ejemplo: "Sencillamente este formato es una mierda...*  

    - **Neutro**: Se asignará esta etiqueta a un comentario si no expresa una opinión clara sobre el nuevo formato. Se entenderan como neutros los comentarios en los que no se determine una idea clara a favor o en contra del nuevo formato.  
      *Ejemplo: "El formato tiene cosas que no me gustan, pero el anterior era muuucho peor"*  

    - **Irrelevante**: Se asignará esta etiqueta a un comentario si no está relacionado con el tema del nuevo formato de la Liga de Campeones. Puede incluir comentarios sobre otros temas, bromas, opiniones propias sobre que se deberia de hacer o respuestas sin contenido relevante. 
      *Ejemplo: "¿Y del formato del bicep de Nacho qué opináis?"*  

```


#### Tareas
Título
Introducción: Formalización y motivación de las preguntas de investigación
Sistema: Descripción del sistema utilizado (incluye preprocesamiento y postprocesamiento)
Datos: corpus y datos utilizados y descripción sobre su tratamiento.
Resultados y análisis: Resultados y análisis de los experimentos
Conclusiones
Referencias

