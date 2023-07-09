### IMPORTAMOS LIBRERIAS

import pandas as pd
import numpy  as np

from fastapi import FastAPI

import uvicorn

from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.utils.extmath           import randomized_svd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise        import linear_kernel

# Ingestamos

data = pd.read_csv("data_set/ds_model.csv")

      ### CREACION DEL MODELO DE RECOMENDACIONES ### 

muestra_aleatoria = data.head(5000) # Utilizamos solo 20 mil filas del datasets 

tfidf = TfidfVectorizer(stop_words='english') #Convertimos el texto en una matriz de caracteristicas numericas para facilitar el calculo de similitudes


tdfid_matrix = tfidf.fit_transform(muestra_aleatoria['overview']) # Analizamos y extraemos las palabras mas importantes con TF-IDF Y creamos una matriz que representa la


cosine_similarity = linear_kernel( tdfid_matrix, tdfid_matrix) # Calculamos la similitud coseno entre todas las descripciones la similitud coseno 
                                                                 # es una medida que nos indica cuanto se parecen dos vectores 
def recomendacion(titulo: str):
    idx = muestra_aleatoria[muestra_aleatoria['title'] == titulo].index[0] # Buscamos el indice titulo en nuestro datasets

    sim_cosine = list(enumerate(cosine_similarity[idx])) # Accedemos a la fila 'idx' de la matriz 'simitulud coseno' enumeramos filas, creamos lista de 
                                                             #tuplas, donde cada tupla contiene el indice y similitud coseno de la pelicula
    

    sim_scores = sorted(sim_cosine, key=lambda x: x[1], reverse=True) # Ordenamos la lista de tuplas en funcion de la similitud coseno de manera descendente,
                                                                         #guardamos resultados en variable sim_scores
    

    similar_indices = [i for i, _ in sim_scores[1:6]] # Creamos lista de las 5 mejores primeras peliculas

    similar_movies = muestra_aleatoria['title'].iloc[similar_indices].values.tolist() # Seleccionamos los titulos segun los indices y los pasamos a una lista
    
    return similar_movies #Retornamos la lista


# name = recomendacion('Toy Story')
# print (name)
