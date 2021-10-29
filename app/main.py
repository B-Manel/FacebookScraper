from fastapi import FastAPI
from databases import Database
from uvicorn import run

database = Database("sqlite:///Facebook.db")
app = FastAPI()


@app.on_event("startup")
async def database_startup():
    await database.connect()


@app.on_event("shutdown")
async def database_shutdown():
    await database.disconnect()


@app.get("/")
async def get_data():
    query = "SELECT * FROM pages"
    results = await database.fetch_all(query=query)

    return results


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
