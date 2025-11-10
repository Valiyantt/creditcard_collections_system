# backend/app/schemas.py
from pydantic import BaseModel, validator
from typing import Optional
from decimal import Decimal
from datetime import datetime


class ClientCreate(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    initial_due: Decimal = Decimal("0.00")

    @validator("initial_due")
    def non_negative_due(cls, v):
        if v < 0:
            raise ValueError("Initial due must be non-negative")
        return v


class ClientRead(BaseModel):
    id: int
    name: str
    email: Optional[str]
    phone: Optional[str]
    initial_due: Decimal
    created_at: datetime
    balance: Decimal  # include computed balance

    class Config:
        orm_mode = True


class PaymentCreate(BaseModel):
    client_id: int
    amount: Decimal
    method: Optional[str] = None
    notes: Optional[str] = None

    @validator("amount")
    def positive_amount(cls, v):
        if v <= 0:
            raise ValueError("Payment amount must be positive")
        return v


class PaymentRead(BaseModel):
    id: int
    client_id: int
    amount: Decimal
    recorded_at: datetime
    method: Optional[str]
    notes: Optional[str]

    class Config:
        orm_mode = True
