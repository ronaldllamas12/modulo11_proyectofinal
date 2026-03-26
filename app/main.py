from fastapi import FastAPI
from routes.router_ping import router as router_prueba
from fastapi.responses import JSONResponse



app = FastAPI()
app.include_router(router_prueba)
@app.get("/")
async def root():
    return JSONResponse({"mensaje":"Api funcionando correctamente"},status_code=200)

