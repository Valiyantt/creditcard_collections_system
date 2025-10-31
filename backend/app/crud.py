# backend/app/crud.py
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from decimal import Decimal
from . import models
from .redis_client import set_cached_balance, get_cached_balance
from typing import Optional

async def create_client(db: AsyncSession, name: str, email: Optional[str], phone: Optional[str], initial_due: Decimal):
    client = models.Client(name=name, email=email, phone=phone, initial_due=initial_due)
    db.add(client)
    await db.commit()
    await db.refresh(client)
    # initialize balance cache: initial_due
    await set_cached_balance(client.id, str(initial_due))
    return client

async def get_client(db: AsyncSession, client_id: int):
    q = await db.execute(select(models.Client).where(models.Client.id == client_id))
    return q.scalar_one_or_none()

async def list_clients(db: AsyncSession, limit: int = 100):
    q = await db.execute(select(models.Client).limit(limit))
    return q.scalars().all()

async def record_payment(db: AsyncSession, client_id: int, amount: Decimal, method: Optional[str], notes: Optional[str]):
    # create payment entry
    payment = models.Payment(client_id=client_id, amount=amount, method=method, notes=notes)
    db.add(payment)
    # commit
    await db.commit()
    await db.refresh(payment)
    # recompute balance and update cache
    balance = await compute_balance(db, client_id)
    await set_cached_balance(client_id, str(balance))
    return payment

async def compute_balance(db: AsyncSession, client_id: int) -> Decimal:
    # initial_due - sum(payments)
    q = await db.execute(
        select(models.Client.initial_due, func.coalesce(func.sum(models.Payment.amount), 0)).join(
            models.Payment, isouter=True
        ).where(models.Client.id == client_id).group_by(models.Client.initial_due)
    )
    row = q.one_or_none()
    if row:
        initial_due, payments_sum = row
        balance = Decimal(initial_due) - Decimal(payments_sum)
        return balance
    # fallback: client not found or no payments
    client = await get_client(db, client_id)
    if client:
        return Decimal(client.initial_due)
    return Decimal("0.00")
