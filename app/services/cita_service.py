from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.cita import Cita
from app.models.horario import Horario
from app.schemas.cita import CitaCreate

def agendar_cita(db: Session, cita_in: CitaCreate, paciente_id: int):
    horario = db.query(Horario).filter(Horario.id == cita_in.horario_id, Horario.disponible == True).first()
    if not horario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El horario no está disponible")
    
    horario.disponible = False
    
    nueva_cita = Cita(
        paciente_id=paciente_id,
        medico_id=cita_in.medico_id,
        horario_id=cita_in.horario_id
    )
    db.add(nueva_cita)
    db.commit()
    db.refresh(nueva_cita)
    return nueva_cita

def obtener_citas_paciente(db: Session, paciente_id: int):
    return db.query(Cita).filter(Cita.paciente_id == paciente_id).all()

def cancelar_cita(db: Session, cita_id: int, paciente_id: int):
    cita = db.query(Cita).filter(Cita.id == cita_id).first()
    if not cita:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
    if cita.paciente_id != paciente_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No puedes cancelar una cita ajena")
    
    cita.estado = "cancelada"
    horario = db.query(Horario).filter(Horario.id == cita.horario_id).first()
    if horario:
        horario.disponible = True
    db.commit()
