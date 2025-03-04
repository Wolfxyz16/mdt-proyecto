# Proyecto Mineria de Datos Textuales

## ¿Qué opinan los espectadores de medios de comunicación alternativos (la media inglesa, mundo maldini) sobre el nuevo formato de la Liga de Campeones?

El fútbol europeo ha sufrido un gran cambio este año. La competición más seguida del mundo entero, la Liga de Campeones de la UEFA, estrenó un nuevo formato donde entre otras cosas se amplian los equipos participantes a treinta y seís. Estos cambios han generado opiniones polarizadas en los espectadores. A su vez estas opiniones han ido cambiando a lo largo que se ha ido desarrollando el torneo, yendo de negativas a positivas. Sin embargo, todavía existen un gran bloque de retractores.

En este proyecto vamos a analizar las **opiniones de espectadores de medios de comunicación alternativos sobre el nuevo formato de la Liga de Campeones**. Para ello vamos a extraer la información de la sección de comentarios de los vídeos de analísis de estos medios de comunicación. Los dos vídeos que vamos a utilizar son:

* [CHAMPIONS Y EL NUEVO FORMATO, ASÍ ES. ¿OS GUSTA? ¿QUÉ PRETENDE LA UEFA? MI OPINIÓN-Mundo Maldini](https://www.youtube.com/watch?v=x822KmLGDsQ) 
* [¿FUNCIONA EL NUEVO FORMATO DE LA CHAMPIONS LEAGUE?-La media inglesa](https://www.youtube.com/watch?v=f0CYxwRY0to) 

Finalmente debido a la cantidad de comentarios en cada video hemos decidido extraer los datos de **La media inglesa**

A la hora de anotar estos datos utilizaremos etiquetas que midan el grado de satisfacción del nuevo formato. Las etiquetas para el análisis de sentimientos serán `POS`, `NEG` y `NT`. También tendremos una etiqueta `IRR` que nos indicará cuando un comentario no tenga que ver con nuestra pregunta de investigación o sea irrelevante.

## Consulta para la obtención de los datos

Para obtener los datos utilizaremos el siguiente script en python que nos ayudará a scrappear la información de la sección de comentarios.

```bash
python prueba-youtube.py
```
⚠️ Es necesario tener chromedriver instalado para poder ejecutar el programa ⚠️ 

## 3. Preprocesamiento y anonimización de los datos.
* Tener en cuenta que, dependiendo de sus datos, es posible que sea necesario eliminar/agregar algunos pasos al preprocesamiento y que es importante adecuar el preprocesamiento al modelo concreto que usamos.

Hemos extraido los comentarios del video y hemos conseguido un conjunto de datos de 464 comentarios. Estos, seran etiquetados por nuestro equipo y podrán tener las siguientes etiquetas:

* Positive [1]
* Neutral [2]
* Negative [3]
* Irrelevant [3]

## 4. Anotar el conjunto de datos (test) para evaluar un modelo
* Elegir las etiquetas adecuadas para responder a la pregunta de investigación.
* Usar LabelStudio para anotar los datos
* Guardar en formato json

Hemos realizado una seleccion de los comentarios en los que si se habla acerca del nuevo formato y hemos obtenido cerca de 150 comentarios, que se usaran en el siguiente paso del trabajo. 

## 5. Dado que no tendrá un conjunto de datos para entrenar un modelo, os aconsejamos usar uno o más de las siguientes opciones:
* Crear un enfoque basado en el léxico
* O crear un conjunto de datos de plata usando emoji/palabras de emoción como pseudoetiquetas (distant supervision)
* Finalmente, también puedes utilizar el aprendizaje por transferencia (transfer learning) si encuentras conjuntos de datos adecuados en otro idioma.

## 6. Evaluar el modelo, usando la métrica adecuada que corresponde a la tarea.
