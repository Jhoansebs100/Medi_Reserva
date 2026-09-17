from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.horario import HorarioCreate, HorarioOut
from app.models.usuario import Usuario
from app.auth.dependencias import exigir_rol
from app.services import horario_service

router = APIRouter(prefix="/horarios", tags=["Horarios"])

@router.post("/", response_model=HorarioOut, status_code=status.HTTP_201_CREATED)
def crear(
    horario_in: HorarioCreate, 
    db: Session = Depends(get_db), 
    medico: Usuario = Depends(exigir_rol(["medico"]))
):
    return horario_service.crear_horario(db, horario_in, medico_id=medico.id)

@router.delete("/{horario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(
    horario_id: int, 
    db: Session = Depends(get_db), 
    medico: Usuario = Depends(exigir_rol(["medico"]))
):
    horario_service.eliminar_horario(db, horario_id, medico_id=medico.id)
