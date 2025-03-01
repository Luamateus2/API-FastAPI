import uvicorn
from fastapi import FastAPI
from contas.routers.contas_pagar import router
app = FastAPI()


@app.get("/")
async def root():
    return{"message":"Hello World"}


app.include_router(router)
if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8006)