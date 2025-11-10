# backend/app/api/__init__.py
from fastapi import APIRouter
from . import clients, payments

# Create a root router that can include all sub-routers
api_router = APIRouter()

api_router.include_router(clients.router, prefix="/clients", tags=["Clients"])
api_router.include_router(payments.router, prefix="/payments", tags=["Payments"])
