from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from .database import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    initial_due = Column(Numeric(scale=2), default=0)  # starting amount owed
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    payments = relationship("Payment", back_populates="client", cascade="all, delete-orphan")


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Numeric(scale=2), nullable=False)
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
    method = Column(String, nullable=True)  # e.g., cash, bank transfer, etc.
    notes = Column(String, nullable=True)

    client = relationship("Client", back_populates="payments")
