import uvicorn
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Drzave(BaseModel):
    ime_drzave: str
    glavni_grad: str
    unMember: bool
    capital: str
    region: str

class CountryStore:
    stored_drzava = {}

async def fetch_rest_countries(name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://restcountries.com/v3.1/name/{name}/")
        return response.json()

@app.get("/async_countries/{name}", response_model=dict)
async def async_countries(name: str):
    country_data = await fetch_rest_countries(name)

   
    print(f"Received country_data: {country_data}")

  
 

    country_details = Drzave(
        ime_drzave=country_data[0].get("name", {}).get("common", ""),
        glavni_grad=country_data[0].get("capital", [""])[0],
        unMember=country_data[0].get("unMember", False),
        capital=country_data[0].get("capital", [""])[0],
        region=country_data[0].get("region", "")
    )

    CountryStore.stored_drzava[name] = country_details

    return {"country_data": country_data, "stored_country": CountryStore.stored_drzava}

@app.get("/country_store", response_model=dict)
async def get_country_store():
    return {"stored_country": CountryStore.stored_drzava}

@app.delete('/delete_country/{name}')
async def delete_country(name: str):
    if name not in CountryStore.stored_drzava:
        raise HTTPException(status_code=404, detail=f"Country {name} not found.")

    deleted_country = CountryStore.stored_drzava.pop(name)
    return {"message": f"Country {deleted_country.ime_drzave} successfully deleted."}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
