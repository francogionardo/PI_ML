from fastapi import FastAPI   # framework para crear API's
from fastapi import Response  # Clase que se usa para enviar respuestas desde los endpoints
import pandas as pd
import json

# Se instancia el APi (Framework de python)
# El API define las rutas, los metodos HTTP, y las fucniones asociadas para el manejo de solicitudes
app = FastAPI()

# Se ingestan los datos y se crea un dataframe
df = pd.read_csv("movies_clean.csv")


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
    respuesta = {
        'cantidad_peliculas': cantidad_peliculas,
        'idioma': Idioma
    }
    
    return respuesta

if __name__ == "__main__":
    import uvicorn   # Biblioteca de python que ejecutará y servirá a la aplicación FastAPi
    # Recibe las solictudes HTTP entrantes y enruta a la aplicación FastApi
    uvicorn.run(app, host="0.0.0.0", port=8000)


# http://localhost:8000/?Idioma=English
