from fastapi import FastAPI
from .database import engine
from . import models
from .routers import auth, posts
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, posts, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API with JWT Authentication")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # para testes, no deploy colocar só domínios confiáveis
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(users.router)
