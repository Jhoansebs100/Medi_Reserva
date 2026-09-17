from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.horario import Horario
from app.schemas.horario import HorarioCreate

def crear_horario(db: Session, horario_in: HorarioCreate, medico_id: int):
    nuevo_horario = Horario(
        medico_id=medico_id,
        fecha_inicio=horario_in.fecha_inicio,
        fecha_fin=horario_in.fecha_fin
    )
    db.add(nuevo_horario)
    db.commit()
    db.refresh(nuevo_horario)
    return nuevo_horario

def eliminar_horario(db: Session, horario_id: int, medico_id: int):
    horario = db.query(Horario).filter(Horario.id == horario_id).first()
    if not horario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Horario no encontrado")
    if horario.medico_id != medico_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No puedes modificar un horario ajeno")
    db.delete(horario)
    db.commit()
