from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

async def fetch_population_data(country_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://127.0.0.1:8002/get_population/{country_name}")

    try:
        response.raise_for_status()
        population_data = response.json()
        return population_data
    except (httpx.HTTPStatusError, httpx.RequestError):
        raise HTTPException(status_code=500, detail="Error fetching population data")

@app.post("/get_population")
async def get_population(country_name: str):
    print(country_name)  # Add this line to print the received data
    response_app3 = await httpx.get(f"http://127.0.0.1:8002/get_population/{country_name}")
    data_app3 = response_app3.json()
    modified_population = data_app3.get("population", 0) * 2
    
    return {"original_population": data_app3.get("population", "N/A"), "modified_population": modified_population}
