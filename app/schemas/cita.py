from pydantic import BaseModel

class CitaCreate(BaseModel):
    medico_id: int
    horario_id: int

class CitaOut(BaseModel):
    id: int
    paciente_id: int
    medico_id: int
    horario_id: int
    estado: str

    class Config:
        from_attributes = True
