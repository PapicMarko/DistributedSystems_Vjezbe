#Vjezba 3 _ 08.11.23.

"""
import asyncio
import random


async def hello_world():
    print("Hello World")


async def task_1():
    print("Task 1: Start")
    await asyncio.sleep(2)
    print("Task 1: End")


async def task_2():
    print("Task 2: Start")
    await asyncio.sleep(3)
    print("Task 2: End")


async def main():
    #Create asynchrounous tasks
    task_1 = asyncio.create_task(task_1())
    task_2 = asyncio.create_task(task_2())

    await asyncio.gather(task_1, task_2)

"""

import asyncio
import aiohttp

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def requestMaker(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
        pokemon_list = [1, 20, 33, 51, 612]
        tasks = [requestMaker(f"https://pokeapi.co/api/v2/pokemon/{x}") for x in pokemon_list]
        result = await asyncio.gather(*tasks)
        for res in result: 
             print(f"Name: ", res["name"])
             print(f"Height is: ", res["height"])
             print(f"Base XP: ", res["base_experience"])
             print()

asyncio.run(main())
