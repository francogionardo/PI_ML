<h1 align='center'>
  <img src="Image/logo.png" alt="Logo del Proyecto" /><br>
   Deployment de un Modelo de Clasificación para un Sistema de Recomendación de Películas
   
    
</h1>
<h2 align='center'
>
Proyecto Individual I

## Introducción:

En este proyecto de Machine Learning, asumiré el rol de un Data Engineer y ML Operations y llevaré a cabo todos los procesos necesarios, desde el tratamiento y recolección de datos hasta el entrenamiento y despliegue del modelo de ML. El objetivo principal es desarrollar un sistema de recomendación de películas basado en técnicas de similitud y algoritmos de Machine Learning.

## Definción de objetivos del proyecto:
---
1. **Generación de API´s que procesan funciones que responden a consultas acerca de las características de películas**: El entregable esta etapa, se exploran los datos disponibles, se realiza un análisis de calidad y se lleva a cabo la limpieza necesaria para prepararlos para el modelado.

2. **Deployment de un modelo de clasificación par un sistema de recomendación de películas**: Aquí se seleccionan las características relevantes para el modelo y se pueden crear nuevas características a partir de las existentes, como la tokenización de texto o la extracción de características numéricas.

---
## Resumen de los procesos:
---
### 1. Proceso de Extracción, Transformación, Carga ( _enlace:_ [ETL ](https://github.com/abelfranco/PI_ML/blob/master/ETL.ipynb))

En el archivo **ETL.py**, se llevó a cabo el proceso de extracción de datos de dos fuentes, la transformación de los datos para su limpieza y preprocesamiento, y finalmente la carga de los datos en un formato adecuado (archivo **ds_clean.csv**) para su posterior análisis y entrenamiento del modelo.

### 2. Análisis Exploratorio de Datos ( _enlace:_ [EDA ](https://github.com/abelfranco/PI_ML/blob/master/EDA.ipynb))

En el notebook **EDA.ipynb**, se realizará un **`INFORME`** de Análisis exhaustivo de los datos y la factiblidad de modelos de clasificación para el caso en estudio. Esto incluirá la visualización de los datos, reducción de dimensionalidad, tratamiento de valores atípicos y la generación de conclusiones relevantes entorno a las variables y la elección del modelo.

### 3. Implementación de API´s ( _enlace:_ [main.py ](https://github.com/abelfranco/PI_ML/blob/master/main.py))

En el archivo **main.py**, se creará una interfaz utilizando la biblioteca **FastAPI y Uvicorn**. Esta interfaz permitirá a los usuarios interactuar con el modelo de Machine Learning, proporcionando los datos de entrada necesarios y obteniendo las predicciones correspondientes.

### 4. Desarrollo del Modelo de Machine Learning ( _enlace:_ [model.py ](https://github.com/abelfranco/PI_ML/blob/master/model.py))

En el archivo **model.py**, se implementará un modelo de Machine Learning utilizando **Similitud de cosenos**. Este modelo se entrenó utilizando los datos preprocesados y preparados durante el EDA (archivo **ds_model.csv**).Finalmente se realizó el deployemnt de la aplicación usando [RENDER ](https://dashboard.render.com/web/srv-cijd6sd9aq01qqirngrg).

---
- _"Cada etapa fué realizada de manera sistemática y documentada adecuadamente en los archivos correspondientes, siguiendo las mejores prácticas de ciencia de datos y ML Operations, para garantizar la reproducibilidad, calidad y mantenibilidad del proyecto"_
---
## Stack Tecnológico
- Scikit learn:
- Python:
- Numpy:
- Pandas:
- FastAPI:
- Uvicorn:
- Render: