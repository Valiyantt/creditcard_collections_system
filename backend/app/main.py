# backend/app/main.py
import os
from fastapi import FastAPI, Depends, HTTPException, status
from decimal import Decimal
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from .database import async_session, engine, Base
from . import models, schemas, crud
import asyncio
from .redis_client import get_cached_balance, set_cached_balance, get_redis

app = FastAPI(title="Collection System API")

# Create tables on startup (for dev). In production, use Alembic migrations.
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # warm redis connection
    await get_redis()

# dependency
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

@app.post("/clients", response_model=schemas.ClientRead, status_code=status.HTTP_201_CREATED)
async def create_client(payload: schemas.ClientCreate, db: AsyncSession = Depends(get_db)):
    client = await crud.create_client(db, payload.name, payload.email, payload.phone, payload.initial_due)
    # include balance
    balance_cached = await get_cached_balance(client.id)
    balance = Decimal(balance_cached) if balance_cached is not None else Decimal(client.initial_due)
    return schemas.ClientRead.from_orm(client).copy(update={"balance": balance})

@app.get("/clients", response_model=List[schemas.ClientRead])
async def list_clients(limit: int = 100, db: AsyncSession = Depends(get_db)):
    clients = await crud.list_clients(db, limit)
    results = []
    for c in clients:
        bal_cached = await get_cached_balance(c.id)
        if bal_cached is None:
            bal = await crud.compute_balance(db, c.id)
            await set_cached_balance(c.id, str(bal))
        else:
            bal = Decimal(bal_cached)
        results.append(schemas.ClientRead.from_orm(c).copy(update={"balance": bal}))
    return results

@app.get("/clients/{client_id}", response_model=schemas.ClientRead)
async def get_client(client_id: int, db: AsyncSession = Depends(get_db)):
    client = await crud.get_client(db, client_id)
    if not client:
        raise HTTPException(404, "Client not found")
    bal_cached = await get_cached_balance(client.id)
    if bal_cached is None:
        bal = await crud.compute_balance(db, client.id)
        await set_cached_balance(client.id, str(bal))
    else:
        bal = Decimal(bal_cached)
    return schemas.ClientRead.from_orm(client).copy(update={"balance": bal})

@app.post("/payments", response_model=schemas.PaymentRead, status_code=status.HTTP_201_CREATED)
async def create_payment(payload: schemas.PaymentCreate, db: AsyncSession = Depends(get_db)):
    client = await crud.get_client(db, payload.client_id)
    if not client:
        raise HTTPException(404, "Client not found")
    payment = await crud.record_payment(db, payload.client_id, payload.amount, payload.method, payload.notes)
    return schemas.PaymentRead.from_orm(payment)

@app.get("/clients/{client_id}/balance")
async def get_balance(client_id: int, db: AsyncSession = Depends(get_db)):
    bal_cached = await get_cached_balance(client_id)
    if bal_cached is not None:
        return {"client_id": client_id, "balance": Decimal(bal_cached)}
    # compute and cache
    bal = await crud.compute_balance(db, client_id)
    await set_cached_balance(client_id, str(bal))
    return {"client_id": client_id, "balance": bal}
