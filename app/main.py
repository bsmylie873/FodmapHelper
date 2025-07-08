from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.init_db import init_db
from app.routes import food
import os

app = FastAPI(
    title="FODMAP Helper API",
    description="API for managing and querying FODMAP food data",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup."""
    # Force reset in development mode
    is_dev = os.getenv("ENVIRONMENT", "development") == "development"
    init_db(force_reset=is_dev)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(food.router) 