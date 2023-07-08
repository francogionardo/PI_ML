<h1 align='center'>
 <b>Proyecto  Individual I</b>
</h1>

***
<h1 align='center'>
<b>Movie Recommendation
🎬🍿</b>
</h1>

<p align="center">
  <img src="Image/logo.png" />
</p>

***
En este proyecto de Machine Learning, asumiré el rol de un Data Engineer y ML Operations y llevaré a cabo todos los procesos necesarios, desde el tratamiento y recolección de datos hasta el entrenamiento y deployment del modelo de ML. 

El proyecto se dividirá en etapas que incluyen: exploración y limpieza de datos, selección y creación de características, elección y ajuste de algoritmos de ML, evaluación y validación del modelo, y finalmente, implementación en un entorno de producción. Cada etapa será realizada de manera sistemática y documentada adecuadamente en los archivos ETL y EDA, siguiendo las mejores prácticas de ciencia de datos, para garantizar la reproducibilidad y calidad del proyecto.

**Proceso de Extracción, Transformación, Carga (ETL)**: En el archivo _ETL.py_, se llevó a cabo el proceso de extracción de datos de diversas fuentes, la transformación de los datos para su limpieza y preparación, y finalmente la carga de los datos en un formato adecuado ( archivo _movies_final.csv_) para su posterior análisis y entrenamiento del modelo.

**Análisis Exploratorio de Datos (EDA)**: En el notebook _EDA.ipynb_, se realizará un análisis exhaustivo de los datos recopilados. Esto incluirá la visualización de los datos, la identificación de patrones, la detección de valores atípicos y la generación de ideas y preguntas relevantes para el problema que estamos abordando.

**Implementación de la Interfaz (main)**: En el archivo _main.py_, se creará una interfaz utilizando la biblioteca FastAPI. Esta interfaz permitirá a los usuarios interactuar con el modelo de machine learning, proporcionando los datos de entrada necesarios y obteniendo las predicciones correspondientes.

**Desarrollo del Modelo de Machine Learning (ml_model)**: En el archivo _ml_model.py_, se implementará un modelo de machine learning utilizando el algoritmo de vecinos más cercanos (K-Nearest Neighbors). Este modelo se entrenará utilizando los datos recopilados y preparados en las etapas anteriores.

#### **Stack Tecnológico**

- Python : Lenguaje base del proyecto
- Numpy : Transformación de datos
- Pandas : Ingesta y transformación de datos
- FastAPI : Procesamiento de los parámetros de funciones
- Uvicorn : Servidor de API's
- Render : Deployment del modelo

**Procesos para la realización del Proyecto en base a los principales entregables:**

#### 1. Deployment de API´s que procesan funciones de acuerdo a consultas específicas predefinidas:

#### 2. Deployment de un Sistema de Recomenadación de Películas usando un modelo de clasificación
