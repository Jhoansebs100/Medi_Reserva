from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.cita import CitaCreate, CitaOut
from app.models.usuario import Usuario
from app.auth.dependencias import obtener_usuario_actual, exigir_rol
from app.services import cita_service

router = APIRouter(prefix="/citas", tags=["Citas"])

@router.post("/", response_model=CitaOut, status_code=status.HTTP_201_CREATED)
def agendar(
    cita_in: CitaCreate, 
    db: Session = Depends(get_db), 
    paciente: Usuario = Depends(exigir_rol(["paciente"]))
):
    return cita_service.agendar_cita(db, cita_in, paciente_id=paciente.id)

@router.get("/mis-citas", response_model=List[CitaOut])
def listar_mis_citas(
    db: Session = Depends(get_db), 
    paciente: Usuario = Depends(obtener_usuario_actual)
):
    return cita_service.obtener_citas_paciente(db, paciente_id=paciente.id)

@router.patch("/{cita_id}/cancelar", status_code=status.HTTP_200_OK)
def cancelar(
    cita_id: int, 
    db: Session = Depends(get_db), 
    paciente: Usuario = Depends(obtener_usuario_actual)
):
    cita_service.cancelar_cita(db, cita_id, paciente_id=paciente.id)
    return {"message": "Cita cancelada correctamente"}
