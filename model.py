import pandas as pd
import numpy  as np

from fastapi import FastAPI

import uvicorn

from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.utils.extmath           import randomized_svd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise        import linear_kernel


df = pd.read_csv("data_set/ds_model.csv")

import nltk
from nltk.tokenize import word_tokenize

# Descargar los recursos necesarios de NLTK (ejecutar solo una vez)
nltk.download('punkt')

# Muestra de datos
overview_sample = "Led by Woody, Andy's toys live happily in his ..."

# Tokenización de la muestra
tokens = word_tokenize(overview_sample)

# Descargar los recursos necesarios de NLTK (ejecutar solo una vez)
nltk.download('punkt')

# Tokenización de la columna "overview"
df['overview_tokens'] = df['overview'].apply(lambda x: word_tokenize(str(x)))

# Tokenización de la columna "title"
df['title_tokens'] = df['title'].apply(lambda x: word_tokenize(str(x)))

''' Vectorización'''

from sklearn.feature_extraction.text import CountVectorizer

# Reemplazar los valores nulos en la columna 'overview' con un valor predeterminado
df['overview'].fillna('Sin descripción', inplace=True)

# Crear una instancia del vectorizador de Bolsa de Palabras con límite máximo de características
vectorizer = CountVectorizer(max_features=100)

# Realizar la tokenización y vectorización de la columna 'overview'
overview_vectors = vectorizer.fit_transform(df['overview_tokens'].apply(lambda x: ' '.join(x)))

# Crear el DataFrame con los vectores de Bolsa de Palabras
overview_df = pd.DataFrame(overview_vectors.toarray(), columns=vectorizer.get_feature_names_out())

# Concatenar el DataFrame de características con el DataFrame original
df_with_features = pd.concat([df, overview_df], axis=1)

''' Entrenamiento '''

from sklearn.metrics.pairwise import cosine_similarity

# Calcular la similitud del coseno entre las películas
similarity_matrix = cosine_similarity(overview_df)

# Ejemplo de recomendación de películas
movie_index = 0  # Índice de la película de referencia
similar_movies = similarity_matrix[movie_index].argsort()[::-1]  # Películas más similares
recommended_movies = similar_movies[1:11]  # Películas recomendadas (excluyendo la película de referencia)

'''Funcion'''

def obtener_recomendaciones(nombre_pelicula):
    # Obtener el índice de la película de referencia
    indice_pelicula = df[df['title'] == nombre_pelicula].index[0]
    
    # Obtener la fila correspondiente a la película de referencia en la matriz de similitud
    similitudes_pelicula = similarity_matrix[indice_pelicula]
    
    # Obtener los índices de las 5 películas más similares (excluyendo la película de referencia)
    indices_recomendadas = similitudes_pelicula.argsort()[-6:-1][::-1]
    
    # Crear una lista con los títulos de las películas recomendadas
    peliculas_recomendadas = []
    for indice in indices_recomendadas:
        titulo = df.loc[indice, 'title']
        peliculas_recomendadas.append(titulo)
    
    return peliculas_recomendadas