from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from app.database import get_db
from app.config import settings
from app.schemas.usuario import UsuarioCreate, UsuarioOut
from app.schemas.token import Token, RefreshTokenInput
from app.services.usuario_service import registrar_paciente, autenticar_usuario
from app.auth.security import create_access_token, create_refresh_token

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register", response_model=UsuarioOut, status_code=status.HTTP_201_CREATED)
def register(usuario_in: UsuarioCreate, db: Session = Depends(get_db)):
    return registrar_paciente(db, usuario_in)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, form_data.username, form_data.password)
    access_token = create_access_token({"sub": str(usuario.id), "rol": usuario.rol})
    refresh_token = create_refresh_token({"sub": str(usuario.id)})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/refresh", response_model=Token)
def refresh(token_in: RefreshTokenInput, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token_in.refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Token no válido para refresh")
        user_id = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Refresh token inválido o expirado")
        
    new_access_token = create_access_token({"sub": user_id})
    new_refresh_token = create_refresh_token({"sub": user_id})
    return {"access_token": new_access_token, "refresh_token": new_refresh_token, "token_type": "bearer"}
