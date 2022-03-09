from multiprocessing import context
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from . import models, schemas
from sqlalchemy.orm import Session 
from .database import engine, get_db
from . import utils
from .config import Settings
from .routers import posts, users, auth, votes

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
async def root():
    return {"connection_status": "ok"}