from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from .database import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=True, index=True)
    initial_due = Column(Numeric(scale=2), default=0)  # starting amount owed
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    payments = relationship("Payment", back_populates="client", cascade="all, delete-orphan")
    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.name}', due={self.initial_due})>"


class Payment(Base):
    __tablename__ = "payments"
    amount = Column(Numeric(precision=12, scale=2), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Numeric(scale=2), nullable=False)
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
    method = Column(String, nullable=True)  # e.g., cash, bank transfer, etc.
    notes = Column(String, nullable=True)
    client = relationship("Client", back_populates="payments")
    def __repr__(self):
        return f"<Payment(id={self.id}, client_id={self.client_id}, amount={self.amount})>"
    