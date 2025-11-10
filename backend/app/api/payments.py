# backend/app/api/payments.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from .. import schemas, crud
from ..database import async_session

router = APIRouter()

# Dependency for DB
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

@router.post("", response_model=schemas.PaymentRead, status_code=status.HTTP_201_CREATED)
async def create_payment(payload: schemas.PaymentCreate, db: AsyncSession = Depends(get_db)):
    client = await crud.get_client(db, payload.client_id)
    if not client:
        raise HTTPException(404, "Client not found")
    payment = await crud.record_payment(db, payload.client_id, payload.amount, payload.method, payload.notes)
    return schemas.PaymentRead.from_orm(payment)
