from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth_router, horario_router, cita_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MediReserva API", version="1.0.0")

app.include_router(auth_router.router)
app.include_router(horario_router.router)
app.include_router(cita_router.router)
