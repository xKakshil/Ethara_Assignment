# Inventory & Order Management System

## Overview

A full-stack Inventory & Order Management System built using FastAPI, React, PostgreSQL, Docker, and Docker Compose.

The application enables businesses to manage products, customers, orders, and inventory through a responsive web interface while enforcing critical business rules such as inventory validation, automatic stock reduction, unique product SKUs, and unique customer emails.

The entire application is containerized and deployed using modern cloud platforms.

---

## Live Application

### Frontend

https://ethara-assignment-bay.vercel.app/

### Backend

https://ethara-assignment-18or.onrender.com

### API Documentation

https://ethara-assignment-18or.onrender.com/docs

---

## Features

### Product Management

* Create products
* View all products
* View product details
* Update products
* Delete products
* Inventory stock tracking
* SKU uniqueness validation

### Customer Management

* Create customers
* View all customers
* View customer details
* Delete customers
* Email uniqueness validation

### Order Management

* Create orders
* View all orders
* View order details
* Delete orders
* Automatic order amount calculation

### Dashboard

* Total Products
* Total Customers
* Total Orders
* Low Stock Products

### Inventory Controls

* Prevent negative stock
* Prevent orders with insufficient inventory
* Automatic stock deduction when orders are placed
* Real-time inventory tracking

### Validation & Error Handling

* Request validation using Pydantic
* Custom exception handling
* Proper HTTP status codes
* Meaningful error messages

---

# Architecture

```text
┌─────────────────────┐
│      React UI       │
│       (Vite)        │
└──────────┬──────────┘
           │ REST API
           ▼
┌─────────────────────┐
│      FastAPI        │
│  Business Logic     │
└──────────┬──────────┘
           │ SQLAlchemy
           ▼
┌─────────────────────┐
│     PostgreSQL      │
│      Database       │
└─────────────────────┘
```

---

# Technology Stack

## Frontend

* React
* React Router
* Axios
* Vite
* CSS3

## Backend

* Python 3.12+
* FastAPI
* SQLAlchemy 2.0
* Pydantic v2
* Alembic

## Database

* PostgreSQL

## DevOps

* Docker
* Docker Compose
* GitHub
* Render
* Vercel

---

# Business Rules Implemented

## Product Rules

* Product SKU must be unique
* Product stock cannot be negative
* Product price must be valid

## Customer Rules

* Customer email must be unique
* Required customer information validation

## Order Rules

* Customer must exist
* Products must exist
* Inventory must be sufficient
* Total amount calculated automatically
* Stock reduced automatically after order creation

---

# API Endpoints

## Products

### Create Product

```http
POST /api/v1/products
```

### Get All Products

```http
GET /api/v1/products
```

### Get Product

```http
GET /api/v1/products/{id}
```

### Update Product

```http
PUT /api/v1/products/{id}
```

### Delete Product

```http
DELETE /api/v1/products/{id}
```

---

## Customers

### Create Customer

```http
POST /api/v1/customers
```

### Get Customers

```http
GET /api/v1/customers
```

### Get Customer

```http
GET /api/v1/customers/{id}
```

### Delete Customer

```http
DELETE /api/v1/customers/{id}
```

---

## Orders

### Create Order

```http
POST /api/v1/orders
```

### Get Orders

```http
GET /api/v1/orders
```

### Get Order

```http
GET /api/v1/orders/{id}
```

### Delete Order

```http
DELETE /api/v1/orders/{id}
```

---

## Dashboard

### Dashboard Summary

```http
GET /api/v1/dashboard
```

Returns:

```json
{
  "total_products": 0,
  "total_customers": 0,
  "total_orders": 0,
  "low_stock_products": []
}
```

---

# Project Structure

```text
Inventory/
│
├── backend/
│   ├── alembic/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── alembic.ini
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── routes/
│   │   └── App.jsx
│   │
│   ├── package.json
│   ├── Dockerfile
│   └── vite.config.js
│
├── docker-compose.yml
├── .env
└── README.md
```

---

# Local Development Setup

## Prerequisites

* Docker
* Docker Compose
* Git

---

## Clone Repository

```bash
git clone <repository-url>
cd Inventory
```

---

## Environment Variables

Create:

```bash
.env
```

Example:

```env
POSTGRES_USER=
POSTGRES_PASSWORD=postgres
POSTGRES_DB=inventor

DB_HOST=postgres
DB_PORT=5432

DATABASE_URL=Your URL HERE
```

---

## Run with Docker Compose

```bash
docker compose up --build
```

---

## Access Application

Frontend:

```text
http://localhost:5173
```

Backend:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

# Database Migrations

Generate Migration

```bash
alembic revision --autogenerate -m "migration_name"
```

Apply Migration

```bash
alembic upgrade head
```

Rollback Migration

```bash
alembic downgrade -1
```

---

# Deployment

## Backend Deployment

Platform:

Render

Features:

* FastAPI Hosting
* PostgreSQL Hosting
* Automatic Deployments
* Environment Variable Management

## Frontend Deployment

Platform:

Vercel

Features:

* React Hosting
* Automatic GitHub Deployments
* Global CDN

---

# Docker Configuration

## Backend Container

* Python Slim Base Image
* FastAPI Application
* Alembic Migrations
* Production Uvicorn Server

## Frontend Container

* Node Alpine Image
* Vite Build Process
* Production Static Assets

## PostgreSQL Container

* Persistent Storage
* Named Volumes
* Environment-based Configuration

---

# Security Considerations

* Environment variables used for configuration
* No hardcoded credentials
* Input validation using Pydantic
* Database constraints
* Exception handling
* CORS configuration

---

# Future Enhancements

* Authentication & Authorization
* JWT Security
* Role-Based Access Control
* Product Categories
* Search & Filtering
* Pagination
* Order Status Tracking
* Audit Logs
* Inventory Reports
* Email Notifications
* Export to Excel/PDF
* CI/CD Pipeline
* Kubernetes Deployment

---

# Author

Kakshil

Software Engineer Candidate

Built as part of the Ethara Software Engineer Technical Assessment.
