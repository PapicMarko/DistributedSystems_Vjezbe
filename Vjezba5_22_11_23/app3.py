from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

async def fetch_country_data(country_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://restcountries.com/v3.1/name/{country_name}")

    try:
        response.raise_for_status()
        country_data = response.json()[0]
        return country_data
    except (httpx.HTTPStatusError, httpx.RequestError, IndexError):
        raise HTTPException(status_code=404, detail="Country not found or population data missing")

@app.get("/get_population/{country_name}")
async def get_population(country_name: str):
    country_info = await fetch_country_data(country_name)

    population = country_info.get("population", "N/A")
    return JSONResponse(content={"population": population})
