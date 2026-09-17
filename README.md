# MediReserva API 🏥

Sistema de gestión y reserva de citas médicas desarrollado con **FastAPI**, **SQLAlchemy** y **PostgreSQL**. Este proyecto implementa una arquitectura multicapa, autenticación basada en tokens JWT con control de acceso por roles (RBAC) y persistencia en base de datos relacional.

---

## 🛠️ Tecnologías Utilizadas

* **Framework:** FastAPI
* **Base de Datos:** PostgreSQL
* **ORM:** SQLAlchemy
* **Seguridad:** JWT (JSON Web Tokens) & Passlib / Bcrypt
* **Servidor ASGI:** Uvicorn

---

## 📋 Estructura del Proyecto

medireserva_api/
├── app/
│   ├── core/         # Configuración de entorno y seguridad
│   ├── models/       # Definición de tablas en SQLAlchemy
│   ├── routers/      # Endpoints de la API (Auth, Usuarios, Citas)
│   ├── schemas/      # Validaciones y serialización con Pydantic
│   ├── services/     # Lógica de negocio
│   ├── database.py   # Conexión a la base de datos
│   └── main.py       # Punto de entrada de la aplicación
├── .env.example      # Plantilla de variables de entorno
├── requirements.txt  # Lista de dependencias del proyecto
└── README.md         # Documentación del proyecto

---

## 🔑 Configuración de Variables de Entorno

Crea un archivo .env en la raíz del proyecto tomando como plantilla el archivo .env.example:

DATABASE_URL=postgresql://postgres:TU_CONTRASEÑA@localhost:5432/medireserva_db
SECRET_KEY=clave_secreta_para_desarrollo
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_MINUTES=43200

Nota: Asegúrate de reemplazar TU_CONTRASEÑA con la clave correspondiente de tu servidor PostgreSQL local.

---

## 🚀 Instrucciones de Ejecución Local

1. Clonar el repositorio:
   git clone https://github.com/Jhoansebs100/Medi_Reserva.git
   cd Medi_Reserva

2. Activar el entorno virtual:
   .\venv\Scripts\activate

3. Instalar dependencias:
   pip install -r requirements.txt

4. Iniciar el servidor con Uvicorn:
   python -m uvicorn app.main:app --reload

---

## 📖 Documentación Interactiva

Una vez que el servidor esté en ejecución, puedes interactuar con todos los endpoints desde la interfaz interactiva de Swagger:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc
