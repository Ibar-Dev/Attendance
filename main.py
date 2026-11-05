#main.py
from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine
from app.router.usuario_router import router as usuario_router

app = FastAPI(title="Attendance", version= "0.1.0")





def crear_base_datos()-> None:
    SQLModel.metadata.create_all(engine)
    print("Base de datos creada con existo")



crear_base_datos()


app.include_router(usuario_router)