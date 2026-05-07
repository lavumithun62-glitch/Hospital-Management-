from fastapi import FastAPI
from app.database.db import Base, engine
from app.routers.auth_router import router as auth_router
from app.routers.appointment_router import router as appointment_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital Management System")

app.include_router(auth_router)
app.include_router(appointment_router)

@app.get("/")
def home():
    return {"message": "API Running Successfully"}
