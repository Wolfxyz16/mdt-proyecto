# Documentación 

## ¿Qué opinan los espectadores de medios de comunicación alternativos sobre el nuevo formato de la Liga de Campeones?

El fútbol europeo ha sufrido un gran cambio este año. La competición más seguida del mundo entero, la Liga de Campeones de la UEFA, estrenó un nuevo formato donde entre otras cosas se amplian los equipos participantes a treinta y seís. Estos cambios han generado opiniones polarizadas en los espectadores. A su vez estas opiniones han ido cambiando a lo largo que se ha ido desarrollando el torneo, yendo de negativas a positivas. Sin embargo, todavía existen un gran bloque de retractores.

En este proyecto vamos a analizar las **opiniones de espectadores de medios de comunicación alternativos sobre el nuevo formato de la Liga de Campeones**, con la inteción de conocer si este nuevo formato es aceptado entre los seguidores de esta competición. Para ello vamos a extraer la información de la sección de comentarios de los vídeos de analísis de medios de comunicación como la media inglesa.

## Extracción de datos

Una vez bien definida la pregunta de investigación con la que trabajaremos, nuestro primer objetivo sera conseguir un conjunto de datos adecuado. Para la obtención de los datos usaremos el script del archivo 'prueba-youtube.py'. Mediante este script, utilizando la libreria webdriver y el ejecutable chromedriver leeremos los comentarios del video que deseamos y crearemos el inicio de la base de datos. 

Como primera idea, decidimos extraer comentarios de distintos videos de medios de comunicación diferentes para obtener mas variedad de datos. Sin embargo, debido a que la cantidad de datos que se extrajeron con un solo video nos parecio suficiente, scrappear mas datos.

[¿FUNCIONA EL NUEVO FORMATO DE LA CHAMPIONS LEAGUE?](https://www.youtube.com/watch?v=kuhhT_cBtFU)

Una vez ejecutado el script, obtuvimos un conjunto de 464 comentarios no etiquetados. Una vez analizado el conjunto de datos, se ha decidido emplear las siguientes etiquetas:

### Guia de anotación
* Positivo: Se asignará la etiqueta positivo a un comentario si en este se expresa una opinión favorable sobre el nuevo formato de la Liga de Campeones. Puede incluir elogios, satisfacción o argumentos que justifiquen el cambio de formato.
    * Ejemplo: "A mi el nuevo formato me encanta, buen vídeo cracks! Por cierto el directo de ayer divertidísimo"  

* Negativo: Se asignará esta etiqueta a un comentario si este expresa una opinión de rechazo sobre el nuevo formato de la Liga de Campeones. Puede incluir críticas, descontento o argumentos que expliquen por qué el cambio no les parece correcto.
    * Ejemplo: "Sencillamente este formato es una mierda...

* Neutro: Se asignará esta etiqueta a un comentario si no expresa una opinión clara sobre el nuevo formato. Se entenderan como neutros los comentarios en los que no se determine una idea clara a favor o en contra del nuevo formato.
    * Ejemplo: "El formato tiene cosas que no me gustan, pero el anterior era muuucho peor"  

* Irrelevante: Se asignará esta etiqueta a un comentario si no está relacionado con el tema del nuevo formato de la Liga de Campeones. Puede incluir comentarios sobre otros temas, bromas, opiniones propias sobre que se deberia de hacer o respuestas sin contenido relevante.
    * Ejemplo: "¿Y del formato del bicep de Nacho qué opináis?"

## Modelo y evaluación

A la hora de empezar con los modelos en nuestro proyecto hemos empezado definiendo unos modelos *baseline* que nos sirven para poder comparar el *F1-score* de estos modelos con el BERT que vamos a entrenar más adelante.

### Lexicones (*baseline*)

El primero de nuestros modelos *baseline* está basado en lexicones, hemos utilizado dos lexicones distintos que se encuentran traducidos al castellano. Estos lexicones son el **NRC Word-Emotion** y el **AFINN Sentiment Lexicon**:

```
NRC
Accuracy:   0.4000
Precision:  0.4159
Recall:     0.4000
F1 Score:   0.4066
```

```
AFINN
Accuracy:   0.4500
Precision:  0.5194
Recall:     0.4500
F1 Score:   0.4486
```

### Majority class (*baseline*)

A la hora de contar cuál es la clase mayoritaria el resultado ha sido la clase `Negative`. Aplicando esta clase a todas las predicciones hemos obtenido los siguientes resultados:

```
Accuracy:   0.4214
Precision:  0.1776
Recall:     0.4214
F1 Score:   0.2499
```

### Random class (*baseline*)

También hemos creado un modelo que asigna las predicciones aleatoriamente. Los resultados de este modelo a lo largo de 50 iteraciones han sido mejores que los obtenidos por la majority class, pero peores que los obtenido por lexicones

```
Accuracy medio:     0.3379
Precision media:    0.3589
Recall medio:       0.3379
F1 Score medio:     0.3422
```

### SVM (*baseline*)

Para convertir los textos en datos números usamos la técnica TF-IDF que le da un valor a las palabras que más salen en un mismo documento. Con esta representación, entrenamos un modelo de tipo SVM para poder clasificar estos comentarios en diferentes sentimientos. Usando este modelo, hemos obtenido estos resultados: 

```
Accuracy:   0.6786
Precision:  0.6773
Recall:     0.6786
F1 Score:   0.6637
```

### Modelo tipo BERT

El modelo que hemos usado está basado en *bert-base-multilingual* que ha sido finetuneado para análisis de sentimientos de reviews de productos. Predice el sentimiento dando un resultado de 1 a 5 estrellas. Nosotros hemos interpretado este número de estrellas como cuánto a favor o en contra está el modelo. Si el modelo predice 1 o 2 estrellas este comentario será de tipo negativo; si devuelve 3 estrellas será de tipo neutral; y si devuelve 4 o 5 estrellas será de tipo positivo. 

Usando este modelo para intentar predecir nuestras etiquetas anotadas nos lleva a los siguientes resultados:

```
Accuracy:   0.6357
Precision:  0.6382
Recall:     0.6357
F1 Score:   0.6355
```

### Modelo tipo BERT v2 (re-entrenado)

Dividimos los conjuntos de entrenamiento y de test (70/30) y volvemos a entrenar al modelo con el conjunto correspondiente. Los resultado que obtuvo el modelo fueron los siguientes:

```
accuracy =  0.7380
precision = 0.7244
recall =    0.7380
F1 =        0.7262
loss =      0.6703
```

## Conclusiones

Los resultados obtenidos muestran una clara mejora en el rendimiento del modelo a medida que avanzamos desde enfoques más simples, como los lexicones y las clases mayoritarias, hasta modelos más avanzados, como SVM y BERT. Mientras que los modelos *baseline* proporcionaron una referencia inicial, fue con la implementación del modelo BERT re-entrenado cuando se lograron los mejores resultados, alcanzando un *F1-score* de 0.7262, lo que indica una capacidad significativa para clasificar correctamente los comentarios.

Sin embargo, a pesar de estas mejoras, el modelo aún presenta ciertas limitaciones. Algunos comentarios ambiguos o con sarcasmo pueden ser difíciles de clasificar con precisión. Además, una mayor cantidad de datos anotados podría mejorar la capacidad del modelo para identificar matices en las opiniones de los espectadores.

En términos del objetivo del estudio, los resultados indican que, aunque la percepción sobre el nuevo formato de la Liga de Campeones ha evolucionado con el tiempo, todavía existe una polarización considerable entre los seguidores. El análisis de sentimiento sugiere que, si bien hay una tendencia creciente a aceptar el nuevo formato, un sector significativo de los aficionados sigue mostrando resistencia al cambio. Esto refleja la complejidad de las opiniones en torno a modificaciones en competiciones deportivas de gran alcance y la importancia de un análisis detallado para comprender la reacción de los seguidores.
