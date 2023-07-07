from fastapi import FastAPI   # framework para crear API's
from fastapi import Response  # Clase que se usa para enviar respuestas desde los endpoints
import pandas as pd
import json

# Se instancia el APi (Framework de python)
# El API define las rutas, los metodos HTTP, y las fucniones asociadas para el manejo de solicitudes
app = FastAPI()

# Se ingestan los datos y se crea un dataframe
df = pd.read_csv("data_set/ds_clean.csv")


@app.get('/peliculas_idioma/{Idioma}')    
# Se ejecuta cuando se hace una solicitud GET a la raiz de la API
# Asi mismo, procesan las solicitudes desde el cliente y generan las respuestas correspondientes
# desde el servidor

# Se crea la función con un argumento con la forma 'Idioma=es'
def peliculas_idioma(Idioma: str):
    # Se filtra el DataFrame por el idioma especificado
    peliculas_filtradas = df[df['original_language'] == Idioma]
    
    # Se obtiene la cantidad de películas encontradas
    cantidad_peliculas = len(peliculas_filtradas)
    
    # Se crea el diccionario de respuesta
    respuesta = {
        'idioma': Idioma,
        'cantidad_peliculas': cantidad_peliculas
        }
    # Convertimos el diccionario a JSON
    json_data = json.dumps(respuesta, indent=4)
    response = Response(content=json_data, media_type="application/json")    
    return response

# # Ejemplo de uso
# resultado = peliculas_idioma('es')
# print(resultado)


@app.get('/peliculas_duracion/{Pelicula}')
def peliculas_duracion(Pelicula: str):
    pelicula_encontrada = df[df['title'] == Pelicula]

    if not pelicula_encontrada.empty:
        duracion = pelicula_encontrada['runtime'].item()
        año = pelicula_encontrada['release_year'].item()
        respuesta = {
            'pelicula': Pelicula,
            'duracion_min': duracion,
            'año':año
        } 

        # Convertimos el diccionario a JSON
        # Convertimos el diccionario a JSON con ensure_ascii=False
        json_data = json.dumps(respuesta, indent=4, ensure_ascii=False)
        response = Response(content=json_data, media_type="application/json")    
                
        return response
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
        ganancia_total = int(franquicia_encontrada['revenue'].sum())
        ganancia_promedio = int(round(franquicia_encontrada['revenue'].mean()))

        respuesta = {
            'franquicia': Franquicia,
            'cantidad_peliculas': cantidad_peliculas,
            'ganancia_total': ganancia_total,
            'ganancia_promedio': ganancia_promedio
        }

        # Convertimos el diccionario a JSON
        json_data = json.dumps(respuesta, indent=4)
        response = Response(content=json_data, media_type="application/json")

        return response
    else:
        return f"No se encontró la franquicia: {Franquicia}"

# # Ejemplo de uso
# resultado3 = franquicia("Toy Story Collection")
# print(resultado3)


@app.get('/peliculas_pais/{Pais}')
def peliculas_pais(Pais: str):
    peliculas_producidas = df[df['production_countries'].str.contains(Pais, na=False, case=False)]
    cantidad_peliculas = len(peliculas_producidas)
    
    data = {
        "pais": Pais,
        "cantidad_peliculas_producidas": cantidad_peliculas
    }

    # Convertimos el diccionario a JSON
    json_data = json.dumps(data, indent=4)
    response = Response(content=json_data, media_type="application/json")    

    return response

# # Ejemplo de uso
# pais_input = "United States"
# resultado4 = peliculas_pais(pais_input)
# print(resultado4)


@app.get('/productoras_exitosas/{Productora}')
def productoras_exitosas(Productora: str):
    peliculas_productora = df[df['production_companies'].str.contains(Productora, na=False, case=False)]
    cantidad_peliculas = int(len(peliculas_productora))
    revenue_total = int(peliculas_productora['revenue'].sum())

    respuesta = {
        'productora': Productora,
        'revenue_total': revenue_total,
        'cantidad_peliculas': cantidad_peliculas
    }

    json_data = json.dumps(respuesta, indent=4)
    response = Response(content=json_data, media_type="application/json")    
    return response

# # Ejemplo de uso
# productora_input = "Warner Bros."
# resultado5 = productoras_exitosas(productora_input)
# print(resultado5)

@app.get('/get_director/{director}')
def get_director(director: str):
    # Creamos un dataset nuevo aplicando el filtro del director y que no este vacio
    df1 = df[df['director'].notna() & df['director'].str.contains(director)]
    # Sumamos los retornos del director
    retorno_dir = df1['return'].sum() 
    cantidad_peliculas = df1.shape[0]    
    data = {
        "director": director,
        "retorno del director": retorno_dir,
        "total de peliculas dirigidas": cantidad_peliculas,
        "peliculas": [{
            "titulo": df1["title"].tolist(),
            "estreno": df1["release_date"].tolist(),
            "retorno": df1["return"].tolist(),
            "presupuesto": df1["budget"].tolist(),
            "ganancias": df1["revenue"].tolist(),
        }]
    }
    # Convert the data dictionary to a JSON string with proper indentation
    json_data = json.dumps(data, indent=4)
    response = Response(content=json_data, media_type="application/json")    
    
    return response

# # Ejemplo de uso
# director_name = 'Forest Whitaker'  # Nombre del director que deseas buscar
# director_info = get_director(director_name)  # 'df' es tu DataFrame con los datos de las películas
# print(director_info)

if __name__ == "__main__":
    import uvicorn   # Biblioteca de python que ejecutará y servirá a la aplicación FastAPi
    # Recibe las solictudes HTTP entrantes y enruta a la aplicación FastApi
    uvicorn.run(app, host="0.0.0.0", port=10000)

# http://localhost:10000/peliculas_idioma/en
# http://localhost:10000/peliculas_duracion/Toy%20Story
# http://localhost:10000/franquicia/Toy%20Story%20Collection
# http://localhost:10000/peliculas_pais/United%20States
# http://localhost:10000/productoras_exitosas/Paramount
# http://localhost:10000/get_director/Forest%20Whitaker

# https://movies-recomendation-system-bgw9.onrender.com/docs#/