from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World! Todo mundo Dançando HA HA HA"}
