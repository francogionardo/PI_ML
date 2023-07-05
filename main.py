from fastapi import FastAPI   # framework para crear API's
from fastapi import Response  # Clase que se usa para enviar respuestas desde los endpoints
import pandas as pd
import json

# Se instancia el APi (Framework de python)
# El API define las rutas, los metodos HTTP, y las fucniones asociadas para el manejo de solicitudes
app = FastAPI()

# Se ingestan los datos y se crea un dataframe
df = pd.read_csv("data_set/movies_clean.csv")


@app.get('/peliculas_idioma/{Idioma}')    # Se define el endpoint raiz en el decorador.
# Decorador = 
# Endpoint = 'peliculas_idioma'. # Idioma=es 
# Se ejecuta cuando se hace una solicitud GET a la raiz de la API
# Asi mismo, procesan las solicitudes desde el cliente y generan las respuestas correspondientes
# desde el servidor

# Se crea la función con un argumento con la forma 'Idioma=es'
def peliculas_idioma(Idioma: str):
    # Se filtra el DataFrame por el idioma especificado
    peliculas_filtradas = df[df['spoken_languages'] == Idioma]
    
    # Se obtiene la cantidad de películas encontradas
    cantidad_peliculas = len(peliculas_filtradas)
    
    # Se crea el diccionario de respuesta
    respuesta = f"{cantidad_peliculas} cantidad de peliculas fueron estrenadas en {Idioma}"
    return respuesta


# idiomas = "English"
# resultado1 = peliculas_idioma(idiomas)
# print(resultado1)


@app.get('/peliculas_duracion/{Pelicula}')
def peliculas_duracion(Pelicula: str):
    pelicula_encontrada = df[df['title'] == Pelicula]

    if not pelicula_encontrada.empty:
        duracion = pelicula_encontrada['runtime'].values[0]
        año = pelicula_encontrada['release_year'].values[0]
        respuesta = f"{Pelicula}. Duración: {duracion}. Año: {año}"
        return respuesta
    else:
        return f"No se encontró la película: {Pelicula}"

# # Ejemplo de uso
# resultado2 = peliculas_duracion("Toy Story")
# print(resultado2)

@app.get('/franquicia/{Franquicia}')
def franquicia(Franquicia: str):
    franquicia_encontrada = df[df['belongs_to_collection'].fillna('') == Franquicia]

    if not franquicia_encontrada.empty:
        cantidad_peliculas = len(franquicia_encontrada)
        ganancia_total = franquicia_encontrada['revenue'].sum()
        ganancia_promedio = round(franquicia_encontrada['revenue'].mean())

        return f"La franquicia {Franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"
    else:
        return f"No se encontró la franquicia: {Franquicia}"

# # Ejemplo de uso
# resultado3 = franquicia("Toy Story Collection")
# print(resultado3)


@app.get('/peliculas_pais/{Pais}')
def peliculas_pais(Pais: str):
    peliculas_producidas = df[df['production_countries'].str.contains(Pais, na=False, case=False)]
    cantidad_peliculas = len(peliculas_producidas)
    
    return f"Se produjeron {cantidad_peliculas} películas en el país {Pais}"

# # Ejemplo de uso
# pais_input = "United States"
# resultado4 = peliculas_pais(pais_input)
# print(resultado4)


@app.get('/productoras_exitosas/{Productora}')
def productoras_exitosas(Productora: str):
    peliculas_productora = df[df['production_companies'].str.contains(Productora, na=False, case=False)]
    cantidad_peliculas = len(peliculas_productora)
    revenue_total = peliculas_productora['revenue'].sum()
    
    return f"La productora {Productora} ha tenido un revenue de {revenue_total} y ha realizado {cantidad_peliculas} películas"

# Ejemplo de uso
productora_input = "Warner Bros."
resultado5 = productoras_exitosas(productora_input)
print(resultado5)


def get_director(nombre_director, df):
    director_movies = []
    retorno_total = 0

    for index, row in df.iterrows():
        director = row['director']
        movies = row['title']
        release_date = row['release_date']
        return_value = row['return']
        budget = row['budget']
        revenue = row['revenue']

        if nombre_director == director:
            director_movies.append({
                'pelicula': movies,
                'fecha_lanzamiento': release_date,
                'retorno': return_value,
                'costo': budget,
                'ganancia': revenue
            })
            retorno_total += return_value

    director_info = {
        'retorno_total': retorno_total,
        'peliculas_dirigidas': director_movies
    }

    return director_info

director_name = 'Forest Whitaker'  # Nombre del director que deseas buscar
director_info = get_director(director_name, df)  # 'df' es tu DataFrame con los datos de las películas

print(director_info)

# if __name__ == "__main__":
#     import uvicorn   # Biblioteca de python que ejecutará y servirá a la aplicación FastAPi
#     # Recibe las solictudes HTTP entrantes y enruta a la aplicación FastApi
#     uvicorn.run(app, host="0.0.0.0", port=8000)


# http://localhost:8000/peliculas_duracion/Titanic
# http://localhost:8000/productoras_exitosas/Paramount
# http://localhost:8000/director/director





