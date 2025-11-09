# backend/app/crud.py
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from decimal import Decimal
from typing import Optional
from . import models
from .redis_client import set_cached_balance, get_cached_balance


# ----------------------------
# Client Operations
# ----------------------------

async def create_client(
    db: AsyncSession,
    name: str,
    email: Optional[str],
    phone: Optional[str],
    initial_due: Decimal
):
    """Create a new client and cache their initial balance."""
    async with db.begin():
        client = models.Client(
            name=name,
            email=email,
            phone=phone,
            initial_due=initial_due
        )
        db.add(client)

    await db.commit()
    await db.refresh(client)

    # Cache initial balance
    await set_cached_balance(client.id, str(initial_due))
    return client


async def get_client(db: AsyncSession, client_id: int):
    """Retrieve a single client by ID."""
    result = await db.execute(
        select(models.Client).where(models.Client.id == client_id)
    )
    return result.scalar_one_or_none()


async def list_clients(db: AsyncSession, limit: int = 100):
    """List all clients up to a limit."""
    result = await db.execute(select(models.Client).limit(limit))
    return result.scalars().all()


async def update_client(
    db: AsyncSession,
    client_id: int,
    name: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None
):
    """Update client details."""
    client = await get_client(db, client_id)
    if not client:
        return None

    if name:
        client.name = name
    if email:
        client.email = email
    if phone:
        client.phone = phone

    await db.commit()
    await db.refresh(client)
    return client


async def delete_client(db: AsyncSession, client_id: int):
    """Delete a client by ID."""
    client = await get_client(db, client_id)
    if client:
        await db.delete(client)
        await db.commit()
    return client


# ----------------------------
# Payment Operations
# ----------------------------

async def record_payment(
    db: AsyncSession,
    client_id: int,
    amount: Decimal,
    method: Optional[str],
    notes: Optional[str]
):
    """Record a new payment and update cached balance."""
    payment = models.Payment(
        client_id=client_id,
        amount=amount,
        method=method,
        notes=notes
    )
    db.add(payment)
    await db.commit()
    await db.refresh(payment)

    # Recalculate and update cached balance
    balance = await compute_balance(db, client_id)
    await set_cached_balance(client_id, str(balance))
    return payment


async def compute_balance(db: AsyncSession, client_id: int) -> Decimal:
    """Compute a client's current balance: initial_due - total_payments."""
    result = await db.execute(
        select(
            models.Client.initial_due,
            func.coalesce(func.sum(models.Payment.amount), 0)
        )
        .join(models.Payment, isouter=True)
        .where(models.Client.id == client_id)
        .group_by(models.Client.initial_due)
    )

    row = result.one_or_none()
    if row:
        initial_due, payments_sum = row
        return Decimal(initial_due) - Decimal(payments_sum)

    # Fallback if no payments exist
    client = await get_client(db, client_id)
    return Decimal(client.initial_due) if client else Decimal("0.00")
