from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from . import models
from .routers import auth, posts, users

# Cria as tabelas no banco, se ainda não existirem
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API with JWT Authentication")

# Middleware para CORS (ajuste os domínios permitidos para produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # para testes, no deploy coloque domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raiz simples para teste
@app.get("/")
async def root():
    return {"message": "API rodando!"}

# Inclui os routers
app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(users.router)
