import datetime
from fastapi import FastAPI, BackgroundTasks
import httpx
import logging
import random
import asyncio


logging.getLogger("httpx").setLevel(logging.WARNING)

app = FastAPI()

# Lock syncronize
log_lock = asyncio.Lock()

logging.basicConfig(filename="pokemon_api_log.txt", level=logging.INFO)

#random 150 pokemona
async def fetch_single_pokemon():
    random_pokemon_id = random.randint(1, 150)

    url = f"https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    return data


async def fetch_pokemon_data_and_log(n):

    # Odaberemo pokemon ID
    pokemons = await asyncio.gather(*[fetch_single_pokemon() for i in range(n)])

    # Feth pokemon API data

    pokemons_cleared = []
    for pokemon in pokemons:
        pokemon_name = pokemon["name"]
        pokemon_types = [type_info["type"]["name"] for type_info in pokemon["types"]]
        pokemons_cleared.append({"name": pokemon_name, "types": pokemon_types})

    # log information for every pokemon in pokemons_cleared along with the current time
    for pokemon in pokemons_cleared:
        pokemon_name = pokemon["name"]
        pokemon_types = pokemon["types"]
        log_message = f"Name - {pokemon_name}, Types - {', '.join(pokemon_types)}"
        logging.info(f"{datetime.datetime.now()} - {log_message}")


@app.get("/fetch-pokemon-and-log/{number}")
async def fetch_pokemon_and_log(background_tasks: BackgroundTasks, number: int):
    """
    Endpoint that triggers a background task to fetch and log data about a random Pokemon.
    """
    # Use BackgroundTasks directly with the asynchronous function
    background_tasks.add_task(fetch_pokemon_data_and_log, number)
    return {
        "message": "Fetching random Pokemon data from the API and logging. Check the log file later."
    }