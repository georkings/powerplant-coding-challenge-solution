# powerplant-challenge/app/main.py

import logging
from fastapi import FastAPI
from app.routers import production_plan

# Logging configuration
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# FastAPI Application Setup
app = FastAPI()

# --- Routers ---
# Include the production_plan router, which handles the /productionplan endpoint.
app.include_router(production_plan.router)
