from pydantic import BaseModel
from datetime import datetime

class HorarioCreate(BaseModel):
    fecha_inicio: datetime
    fecha_fin: datetime

class HorarioOut(BaseModel):
    id: int
    medico_id: int
    fecha_inicio: datetime
    fecha_fin: datetime
    disponible: bool

    class Config:
        from_attributes = True
