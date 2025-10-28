# Credit Card Collections System

![License](https://img.shields.io/badge/license-MIT-green)

A modular **Credit Card Operations System** built with **Python, FastAPI, PostgreSQL, and Redis**.  
This project serves as a foundation for managing credit card client accounts, payments, and collections, designed to be scalable for additional modules such as **Billing** and **Fraud Management**.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [License](#license)

---

## Overview
This system provides a backend API for managing credit card clients and collections.  
Key goals include:
- Tracking client balances and payments
- Fast balance lookups using Redis caching
- Scalable modular design to add **Billing** and **Fraud Detection** modules in future phases

---

## Features
- **Clients Management**: Add, update, delete, and list clients  
- **Payments Management**: Record payments with method, notes, and timestamp  
- **Collections Module**: Automated balance computation and caching  
- **API Documentation**: Interactive OpenAPI docs via FastAPI  
- **Dockerized Environment**: PostgreSQL and Redis ready-to-use  

---

## Architecture
FastAPI Backend
│
├─ Modules/
│ ├─ Collections/ --> Client & Payment logic
│ ├─ Billing/ --> Future
│ └─ Fraud/ --> Future
│
├─ Database/ --> PostgreSQL (source of truth)
├─ Cache/ --> Redis (fast balance lookups)
└─ Docker Compose --> Local dev environment

---
## Tech Stack
- **Backend**: Python 3.11+, FastAPI (async)
- **Database**: PostgreSQL (async via SQLAlchemy + asyncpg)
- **Cache**: Redis (aioredis)
- **Containerization**: Docker, Docker Compose
- **Schema & Validation**: Pydantic
- **Documentation**: OpenAPI (Swagger UI)

---

## Setup & Installation

### 1. Clone Repository
```bash```
```git clone https://github.com/yourusername/creditcard_collections_system.git```
```cd creditcard_collections_system```

### 2. Start Services via Docker Compose
```env```
```docker-compose up --build```
- FastAPI API: http://localhost:8000/docs
- PostgreSQL: localhost:5432
- Redis: localhost:6379

### 3. Environment Variables

Set the following (default values in docker-compose):
```DATABASE_URL=postgresql+asyncpg://collector:collectorpass@db/collections ```
```REDIS_URL=redis://redis:6379/0 ```

---
Usage
Create a Client
```curl -X POST "http://localhost:8000/clients" \```
```-H "Content-Type: application/json" \```
```-d '{"name":"Acme Corp","email":"acct@acme.test","phone":"0917","initial_due":"10000.00"}'```

Record a Payment
```curl -X POST "http://localhost:8000/payments" \```
```-H "Content-Type: application/json" \```
```-d '{"client_id":1,"amount":"2500.00","method":"bank transfer","notes":"partial payment"}'```

Get Client Balance
```curl "http://localhost:8000/clients/1/balance"```

View All Clients
```curl "http://localhost:8000/clients"```
Interactive API documentation is available at: http://localhost:8000/docs

---
Roadmap

✅ Collections Module (current)

- 🔜 Billing Module: credit card statements, invoices, scheduled charges
- 🔜 Fraud Detection Module: transaction anomaly detection, alerts, blacklists
- 🔜 Web Dashboard: React frontend for collectors and admins
- 🔜 Authentication & Role-Based Access Control (JWT/OAuth2)

---
License
This project is licensed under the MIT License.



