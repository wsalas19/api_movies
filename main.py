from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from functions import peliculas_mes, peliculas_dia, peliculas_pais, franquicia, productoras, retorno

app = FastAPI()



origins = [
    #cuando hayas hecho el deploy, agrega la url del deploy a esta lista
    #"https://deployURLexample.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Movie Recommendation API"}


#Endpoints

#Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron 
# ese mes (nombre del mes, en str, ejemplo 'enero') historicamente
@app.get("/movies/month/{month}")
async def movies_month(month):
    return peliculas_mes(month)


#Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron 
# ese dia (de la semana, en str, ejemplo 'lunes') historicamente
@app.get("/movies/day/{day}")
async def movies_day(day):
    return peliculas_dia(day)


#Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
@app.get("/movies/franchise/{franchise_name}")
async def movies_franchise(franchise_name:str):
    return franquicia(franchise_name)


#Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo
@app.get("/movies/country/{country}")
async def movies_country(country):
    return peliculas_pais(country)


#Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron
@app.get("/movies/producer/{producer}")
async def movies_producer(producer):
    return productoras(producer)


#'Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo
@app.get("/movies/info/{movie_name}")
async def movies_info(movie_name:str):
    return retorno(movie_name)

#Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores
@app.get("/movies/recommend/{movie_title}")
async def movies_recommend(movie_title):
    # here goes the logic
    #
    #
    return {'lista recomendada': [movie_title]}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)










