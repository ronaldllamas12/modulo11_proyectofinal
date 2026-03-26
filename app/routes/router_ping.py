from fastapi import APIRouter
from fastapi.responses import JSONResponse




router= APIRouter()



@router.get("/ping")
async def get_pong():
    return JSONResponse({"mensaje": "pong"},status_code=200)