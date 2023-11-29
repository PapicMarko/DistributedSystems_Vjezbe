from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/{name}")
async def read_item(name: str):
    response_app2 = httpx.post(f"http://127.0.0.1:8001/get_population", json=name)


    data_app2 = response_app2.json()

    original_population = data_app2.get("original_population", "N/A")
    modified_population = data_app2.get("modified_population", "N/A")
    
    return {"original_population": original_population, "modified_population": modified_population}
